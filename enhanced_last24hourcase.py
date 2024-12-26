#!/usr/bin/python3

import requests
import base64
import json
from urllib.parse import urlunparse
from datetime import datetime, timezone, timedelta

# Suppress HTTPS warnings (not recommended in production)
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
#    print(f"Status Code (Access Token): {res.status_code}")
    return res.json()["access_token"]

def getCases(token):
    """
    Retrieve cases from the API using the provided access token.
    """
    headers = {"Authorization": "Bearer " + token}
    
    # Calculate time range for the last 24 hours in UTC+7
    local_timezone = timezone(timedelta(hours=7))
    now_local = datetime.now(local_timezone)
    epoch_now = int(now_local.timestamp() * 1000)  # in milliseconds
    epoch_start = int((now_local - timedelta(hours=24)).timestamp() * 1000)  # 24 hours ago in UTC+7

    # Construct the URL with query parameters
    url = f"https://{HOST}/connect/api/v1/cases?FROM~created_at={epoch_start}&TO~created_at={epoch_now}&sort=created_at&order=desc&page=1&per_page=2&status=New"
    res = requests.get(url, headers=headers, verify=False)
#    print(f"Status Code (Get Cases): {res.status_code}")

    # Attempt to parse JSON response
    try:
        response_json = res.json()
#        print("Raw JSON response:", json.dumps(response_json, indent=4))
        return response_json
    except json.JSONDecodeError:
        print("Failed to decode JSON response for cases")
        return {}

# Function to convert epoch time to a readable date-time format
def convert_epoch_to_datetime(epoch_time):
    local_timezone = timezone(timedelta(hours=7))  # UTC+7 timezone
    return datetime.fromtimestamp(epoch_time / 1000, tz=local_timezone).strftime('%Y-%m-%d %H:%M:%S')

def displayCases(cases):
    print(f"Jumlah Case      : {cases['data']['total']}")
    for case in cases['data']['cases']:
        print(f"Case ID          : {case['_id']}")
        print(f"Closed           : {convert_epoch_to_datetime(case['closed']) if case['closed'] else 'N/A'}")
        print(f"Created At       : {convert_epoch_to_datetime(case['created_at'])}")
        print(f"Created By       : {case['created_by']}")
        print(f"Customer ID      : {case['cust_id']}")
        print(f"Modified At      : {convert_epoch_to_datetime(case['modified_at']) if case['modified_at'] else 'N/A'}")
#        print(f"Modified By      : {case['modified_by']}")
        print(f"Name             : {case['name']}")
        print(f"Score            : {case['score']}")
        print(f"Status           : {case['status']}")
        print(f"Severity         : {case['severity']}")
#        print(f"Tags             : {', '.join(case['tags']) if case['tags'] else 'N/A'}")
        print(f"Ticket ID        : {case['ticket_id']}")
#        print(f"Version          : {case['version']}")
        print(f"Created By Name  : {case['created_by_name']}")
        print(f"Modified By Name : {case['modified_by_name']}")
        print(f"Assignee Name    : {case['assignee_name']}")
        print(f"Tenant Name      : {case['tenant_name']}")
        print("---------------------------------------------------")

if __name__ == "__main__":
    # Step 2: Use getAccessToken with supplied credentials to generate JWT
    jwt = getAccessToken(userid, refresh_token)

    # Step 3: Use JWT token to call public API
    cases = getCases(jwt)
#    print("Berikut daftar cases yang belum di Handle")
    displayCases(cases)
    print("Punggawa Bot 24/7")
