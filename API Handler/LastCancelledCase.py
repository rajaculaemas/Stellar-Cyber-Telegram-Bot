#!/usr/bin/python3

import requests
import base64
from urllib.parse import urlunparse
from datetime import datetime, timedelta, timezone
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
    
    # Mendapatkan waktu sekarang dan 24 jam sebelumnya dalam UTC
    now_utc = datetime.now(timezone.utc)
    epoch_now = int(now_utc.timestamp() * 1000)  # waktu saat ini dalam milidetik
    epoch_24h_ago = int((now_utc - timedelta(hours=24)).timestamp() * 1000)  # 24 jam yang lalu

    # Debug: Print epoch times
#    print(f"Epoch Now: {epoch_now}, Epoch 24h Ago: {epoch_24h_ago}")

    # Menyusun URL dengan filter waktu created_at
    url = urlunparse(("https", HOST, f"/connect/api/v1/cases?tenant_id=<tenentID or custID>?min_score=50&status=Cancelled&sort=created_at&order=desc&limit=5", "", "", ""))
    
    # Debug URL
#    print(f"Request URL: {url}")

    res = requests.get(url, headers=headers, verify=False)
#    print(res.status_code)
    
    # Check response for debugging
    if res.status_code != 200:
        print("Failed to retrieve cases:", res.text)
    
    return res.json()

# Fungsi untuk mengonversi Unix Time ke Date-Time
def convert_epoch_to_datetime(epoch_time):
    return datetime.fromtimestamp(epoch_time / 1000, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

def displayCases(cases):
    print(f"Jumlah Case      : {cases['data']['total']}")
    for case in cases['data']['cases']:
        print(f"cases id         : {case['_id']}")
        print(f"closed           : {convert_epoch_to_datetime(case['closed'])}")
        print(f"created_at       : {convert_epoch_to_datetime(case['created_at'])}")
        print(f"created_by       : {case['created_by']}")
        print(f"cust_id          : {case['cust_id']}")
        print(f"modified_at      : {convert_epoch_to_datetime(case['modified_at']) if case['modified_at'] else ''}")
#        print(f"modified_by      : {case['modified_by']}")
        print(f"name             : {case['name']}")
        print(f"score            : {case['score']}")
        print(f"status           : {case['status']}")
        print(f"severity         : {case['severity']}")
#        print(f"tags             : {', '.join(case['tags']) if case['tags'] else ''}")
        print(f"ticket id        : {case['ticket_id']}")
#        print(f"version          : {case['version']}")
        print(f"created by       : {case['created_by_name']}")
        print(f"modified by      : {case['modified_by_name']}")
        print(f"assignee name    : {case['assignee_name']}")
        print(f"tenant name      : {case['tenant_name']}")
        print("---------------------------------------------------")

if __name__ == "__main__":
    # Mendapatkan token akses
    jwt = getAccessToken(userid, refresh_token)

    # Mengambil data kasus yang dibuat dalam 24 jam terakhir
    cases = getCases(jwt)
#    print("------------ call result of /connect/api/v1/cases -------------")
    if 'data' in cases and cases['data']['total'] > 0:
        displayCases(cases)
    else:
        print("Tidak ada data yang ditemukan")
#    print("------- end api results --------")
