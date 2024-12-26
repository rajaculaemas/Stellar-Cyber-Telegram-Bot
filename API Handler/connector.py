#!/usr/bin/python3

import requests
import base64
import json
from urllib.parse import urlunparse
from datetime import datetime, timezone, timedelta

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
#    print(res.status_code)
    return res.json()["access_token"]

def getCases(token):
    headers = {"Authorization": "Bearer " + token}
    url = urlunparse(("https", HOST, "/connect/api/v1/connectors?cust_id=<tenentID or custID>", "", "", ""))
    res = requests.get(url, headers=headers, verify=False)
#    print(res.status_code)
    return res.json()

def convert_timestamp(timestamp):
    # Mengubah timestamp menjadi format waktu biasa dengan timezone-aware (UTC)
    utc_time = datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc)
    return utc_time.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":

    # Step 2: Use getAccessToken with supplied credentials to generate JWT
    jwt = getAccessToken(userid, refresh_token)

    # Step 3: use JWT token to call public API
    cases = getCases(jwt)
    
    # Mengambil jumlah connector
    total_connectors = cases.get('total', 0)
    print(f"Jumlah Connector : {total_connectors}")
    
    # Menampilkan detail untuk setiap connector
    for i, connector in enumerate(cases.get('connectors', []), 1):
        print(f"\nConnector {i}")
        print(f"Type : {connector.get('type')}")
        print(f"ID : {connector.get('_id')}")
        print(f"Category : {connector.get('category')}")
#        print(f"Created at : {convert_timestamp(connector.get('created_at', 0))}")
        print(f"Tenant ID : {connector.get('tenantid')}")
        print(f"Collect : {connector.get('is_collect')}")
        print(f"Respond : {connector.get('is_respond')}")
        print(f"Last Activity : {convert_timestamp(connector.get('last_activity', 0))}")
        print(f"Last Data Received : {convert_timestamp(connector.get('last_data_received', 0))}")
#        print(f"Modified at : {convert_timestamp(connector.get('modified_at', 0))}")
        print(f"Name : {connector.get('name')}")
        print(f"Run On : {connector.get('run_on')}")
        print(f"Status Time          : {convert_timestamp(connector.get('status', {}).get('status_time', 0))}")
        print(f"Version : {connector.get('version')}")
        print("=" * 50)
