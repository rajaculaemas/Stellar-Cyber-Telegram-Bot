#!/usr/bin/python3

import requests
import base64
import json
from urllib.parse import urlunparse
from datetime import datetime, timezone, timedelta
import pytz
import sys
import calendar

requests.packages.urllib3.disable_warnings()

# Step 1
# Tambahkan IP/hostname, userid, dan refresh token dari GUI stellar cyber anda
HOST = "<your stellar cyber IP/domain>"
userid = "<stellar cyber user id>"
refresh_token = "<stellar cyber refresh token>"

def getAccessToken(userid, refresh_token):
    auth = base64.b64encode(bytes(userid + ":" + refresh_token, "utf-8")).decode("utf-8")
    headers = {
        "Authorization": "Basic " + auth,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    url = urlunparse(("https", HOST, "/connect/api/v1/access_token", "", "", ""))
    res = requests.post(url, headers=headers, verify=False)
    return res.json().get("access_token")

def convert_timestamp_to_datetime(timestamp):
    if isinstance(timestamp, str):
        try:
            timestamp = int(timestamp)  # Convert string to integer
        except ValueError:
            return None
    if isinstance(timestamp, (int, float)):
        return datetime.fromtimestamp(timestamp / 1000, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    return None

def getCases(token, status_filter=None, tenantid_filter=None, start_time=None, end_time=None):
    headers = {"Authorization": "Bearer " + token, 'content-type': 'application/json'}
    
    # Time zone UTC+7
    tz = pytz.timezone('Asia/Jakarta')

    # Generate query based on time range
    query = {
        "size": 10000,
        "query": {
            "bool": {
                "must": []
            }
        }
    }

    if status_filter:
        query["query"]["bool"]["must"].append({"match": {"event_status": status_filter}})
    
    if tenantid_filter:
        query["query"]["bool"]["must"].append({"match": {"tenantid": tenantid_filter}})
    
    if start_time and end_time:
        query["query"]["bool"]["must"].append({
            "range": {
                "timestamp": {
                    "gte": start_time,
                    "lte": end_time,
                    "format": "strict_date_time"
                }
            }
        })

    # Send the request
    url = urlunparse(("https", HOST, "/connect/api/data/aella-ser-*/_search", "", "", ""))
    res = requests.get(url, headers=headers, json=query, verify=False)

    if res.status_code != 200:
        print(f"Error: API response error. Status Code: {res.status_code}")
        return []

    # Process the response data
    data = res.json()
    if 'hits' in data and 'hits' in data['hits']:
        total_hits = data['hits']['total']['value']
        print(f"Total Alert: {total_hits}")
        if total_hits == 0:
            print("No data found matching the criteria.")
            return []

        filtered_cases = []
        for case in data['hits']['hits']:
            _index = case["_index"]
            _id = case["_id"]
            severity = case["_source"].get("severity", "")
            event_status = case["_source"].get("event_status", "")
            alert_type = case["_source"].get("xdr_event", {}).get("display_name", "")
            appid_name = case["_source"].get("appid_name", "")
            engid_name = case["_source"].get("engid_name", "")
            fidelity = case["_source"].get("fidelity", "")
            srcip = case["_source"].get("srcip", "")
            srcip_reputation = case["_source"].get("srcip_reputation", "")
            alert_time = None

            if "stellar" in case["_source"] and "alert_time" in case["_source"]["stellar"]:
                alert_time = convert_timestamp_to_datetime(case["_source"]["stellar"]["alert_time"])
            if not alert_time and "alert_time" in case["_source"]:
                alert_time = convert_timestamp_to_datetime(case["_source"]["alert_time"])

            tenant_name = case["_source"].get("tenant_name", "")
            assignee_time = None
            closed_time = None
            for action in case["_source"].get("user_action", {}).get("history", []):
                if "Event assignee changed" in action["action"] and assignee_time is None:
                    assignee_time = convert_timestamp_to_datetime(action.get("action_time"))
                if action["action"] == "Status changed to Closed" and closed_time is None:
                    closed_time = convert_timestamp_to_datetime(action.get("action_time"))
                if assignee_time and closed_time:
                    break

            comment_user = None
            comment = None
            if case["_source"].get("comments"):
                comment_user = case["_source"]["comments"][0].get("comment_user", "")
                comment = case["_source"]["comments"][0].get("comment", "")

            filtered_cases.append({
                "Alert ID": _id,
                "Alert Time": alert_time,
                "Closed Time": closed_time,
                "Severity": severity,
                "Event Status": event_status,
                "Alert Type": alert_type,
                "Assignee Time": assignee_time,
                "Comment": comment,
                "Tenant Name": tenant_name
            })

        return filtered_cases
    return []

def calculate_sla(cases):
    sla_summary = {
        "< 10 Minutes": 0,
        "< 30 Minutes": 0,
        "< 60 Minutes": 0,
        "< 90 Minutes": 0,
        "< 120 Minutes": 0,
        "> 120 Minutes": 0
    }

    for case in cases:
        alert_time = case.get("Alert Time")
        closed_time = case.get("Closed Time")
        
        if alert_time and closed_time:
            alert_time = datetime.strptime(alert_time, '%Y-%m-%d %H:%M:%S')
            closed_time = datetime.strptime(closed_time, '%Y-%m-%d %H:%M:%S')
            diff = (closed_time - alert_time).total_seconds() / 60  # in minutes

            if diff < 10:
                sla_summary["< 10 Minutes"] += 1
            elif diff < 30:
                sla_summary["< 30 Minutes"] += 1
            elif diff < 60:
                sla_summary["< 60 Minutes"] += 1
            elif diff < 90:
                sla_summary["< 90 Minutes"] += 1
            elif diff < 120:
                sla_summary["< 120 Minutes"] += 1
            else:
                sla_summary["> 120 Minutes"] += 1

    return sla_summary

def get_date_range(time_filter):
    tz = pytz.timezone('Asia/Jakarta')
    now = datetime.now(tz)

    if time_filter == "today":
        start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_day = now
        return start_of_day.isoformat(), end_of_day.isoformat()

    elif time_filter == "yesterday":
        yesterday = now - timedelta(days=1)
        start_of_day = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_day = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999)
        return start_of_day.isoformat(), end_of_day.isoformat()

    elif time_filter == "weekly":
        start_of_week = now - timedelta(days=now.weekday())  # Monday of current week
        end_of_week = start_of_week + timedelta(days=6)  # Sunday of current week
        start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_week = end_of_week.replace(hour=23, minute=59, second=59, microsecond=999999)
        return start_of_week.isoformat(), end_of_week.isoformat()

    elif time_filter == "monthly":
        # Start of current month
        start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        
        # End of current month (using calendar to get the last day of the month)
        last_day_of_month = calendar.monthrange(now.year, now.month)[1]
        end_of_month = now.replace(day=last_day_of_month, hour=23, minute=59, second=59, microsecond=999999)
        
        return start_of_month.isoformat(), end_of_month.isoformat()

    return None, None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 slacalculation.py <TimeFilter>")
        sys.exit(1)

    time_filter = sys.argv[1].lower()

    # Filter status and tenant ID
    status_filter = "Closed"
    tenantid_filter = "<your tenantID>"

    start_time, end_time = get_date_range(time_filter)
    if start_time and end_time:
        token = getAccessToken(userid, refresh_token)
        # Memanggil getCases dengan filter yang telah ditetapkan
        cases = getCases(token, status_filter=status_filter, tenantid_filter=tenantid_filter, start_time=start_time, end_time=end_time)
        sla_summary = calculate_sla(cases)

        print(f"SLA Summary untuk filter {time_filter.capitalize()}:")
        for sla, count in sla_summary.items():
            print(f" Alert Handling {sla}: {count}")
    else:
        print("Invalid time filter.")

if __name__ == "__main__":
    main()
