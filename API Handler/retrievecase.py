#!/usr/bin/python3

import requests
import base64
import json
from urllib.parse import urlunparse
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
    print(res.status_code)
    return res.json()["access_token"]


def getCases(token):
    headers = {"Authorization": "Bearer " + token}
    url = urlunparse(("https", HOST, "/connect/api/v1/cases?limit=5&sort=score&order=desc", "", "", ""))
    res = requests.get(url, headers=headers, verify=False)
    print(res.status_code)
    return res.json()

def displayCases(cases):
    print(f"Jumlah Case      : {cases['data']['total']}")
    for case in cases['data']['cases']:
        print(f"cases id         : {case['_id']}")
#        print(f"acknowledged     : {case['acknowledged']}")
#        print(f"assignee         : {case['assignee']}")
        print(f"closed           : {case['closed']}")
#        print(f"created_at       : {case['created_at']}")
#        print(f"created_by       : {case['created_by']}")
        print(f"cust_id          : {case['cust_id']}")
#        print(f"modified_at      : {case['modified_at']}")
#        print(f"modified_by      : {case['modified_by']}")
        print(f"name             : {case['name']}")
        print(f"score            : {case['score']}")
#        print(f"size             : {case['size']}")
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
#    print("------------ jwt -------------")
#    print(jwt)
#    print("------------ jwt  end -------------")

    # Step 3: use JWT token to call public API
    cases = getCases(jwt)
    print("------------ call result of /connect/api/v1/cases -------------")
   #print(cases)
    displayCases(cases)
    print("------------ end api results -------------")