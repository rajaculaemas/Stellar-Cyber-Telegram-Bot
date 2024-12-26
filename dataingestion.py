#!/usr/bin/python3

import requests
import base64
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
    return res.json()["access_token"]

def getCases(token):
    headers = {"Authorization": "Bearer " + token}
    url = urlunparse(("https", HOST, "/connect/api/v1/storage-usages?aggr_type=tenant&cust_id=<tenentID or custID>", "", "", ""))
    res = requests.get(url, headers=headers, verify=False)
    return res.json()

def print_last_five_cases(cases):
    # Menampilkan 5 data terakhir dengan format yang diminta
    print("Berikut Data Ingestion 5 hari terakhir :")
    
    # Pertama-tama urutkan seluruh data berdasarkan tanggal (time)
    all_entries = cases['data']
    all_entries.sort(key=lambda x: x['time'])  # Mengurutkan berdasarkan tanggal
    
    # Ambil 5 data terakhir setelah pengurutan
    last_five_entries = all_entries[-5:]  # Mengambil 5 data terakhir setelah diurutkan

    for entry in last_five_entries:  # Menggunakan urutan yang sudah diurutkan
        print(f"Date\t\t: {entry['time'][:10]}")  # Mengambil hanya bagian tanggal
        print(f"Total Usage\t: {entry['total_usage']:.2f} GB")
        for usage in entry['usages']:
            print(f"Tenant\t\t: {usage['tenant_name']}")
        print("-" * 60)  # Garis pemisah antar entri

if __name__ == "__main__":
    # Step 2: Use getAccessToken with supplied credentials to generate JWT
    jwt = getAccessToken(userid, refresh_token)

    # Step 3: Use JWT token to call public API
    cases = getCases(jwt)
    print_last_five_cases(cases)  # Menggunakan fungsi baru untuk mencetak 5 data terakhir
