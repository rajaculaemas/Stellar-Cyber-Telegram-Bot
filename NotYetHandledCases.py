#!/usr/bin/python3

import requests
import base64
import json
from urllib.parse import urlunparse
from datetime import datetime, timezone# Import datetime untuk konversi waktu
requests.packages.urllib3.disable_warnings()

# Step 1
# Add DP IP/hostname, userid, and refresh token from GUI here
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
#    print(res.status_code)
    return res.json()["access_token"]

def getCases(token):
    headers = {"Authorization": "Bearer " + token}
    url = urlunparse(("https", HOST, "/connect/api/v1/cases?cust_id=<tenentID or custID>?alerts?view=hits&limit=15&sort=created_at&order=desc", "", "", ""))
    res = requests.get(url, headers=headers, verify=False)
#    print(res.status_code)
    return res.json()

# Fungsi untuk mengonversi Unix Time menjadi Date-Time biasa

def convert_epoch_to_datetime(epoch_time):
    # Menggunakan timezone-aware datetime dengan UTC
    return datetime.fromtimestamp(epoch_time / 1000, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

def displayCases(cases):
    print(f"Jumlah Case      : {cases['data']['total']}")
    for case in cases['data']['cases']:
        print(f"cases id         : {case['_id']}")
        print(f"closed           : {case['closed']}")
        print(f"created_at       : {convert_epoch_to_datetime(case['created_at'])}")
        print(f"created_by       : {case['created_by']}")
        print(f"cust_id          : {case['cust_id']}")
        print(f"modified_at      : {convert_epoch_to_datetime(case['modified_at']) if case['modified_at'] else ''}")
        print(f"modified_by      : {case['modified_by']}")
        print(f"name             : {case['name']}")
        print(f"score            : {case['score']}")
        print(f"status           : {case['status']}")
        print(f"severity         : {case['severity']}")
        print(f"tags             : {', '.join(case['tags']) if case['tags'] else ''}")
        print(f"ticket id        : {case['ticket_id']}")
        print(f"version          : {case['version']}")
        print(f"created by       : {case['created_by_name']}")
        print(f"modified by      : {case['modified_by_name']}")
        print(f"assignee name    : {case['assignee_name']}")
        print(f"tenant name      : {case['tenant_name']}")
        print("---------------------------------------------------")

if __name__ == "__main__":
    # Step 2: Use getAccessToken with supplied credentials to generate JWT
    jwt = getAccessToken(userid, refresh_token)

    # Step 3: use JWT token to call public API
    cases = getCases(jwt)
#    print("Berikut daftar cases yang belum di Handle")
    displayCases(cases)
    print("Punggawa Bot 24/7")
