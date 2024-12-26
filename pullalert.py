#!/usr/bin/python3

import sys  # Menambahkan untuk menangani argumen dari baris perintah
import requests
import base64
import json
from urllib.parse import urlunparse
from datetime import datetime, timezone
import pytz

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
    # Memastikan timestamp adalah integer, jika berupa string, konversi ke integer
    if isinstance(timestamp, str):
        try:
            timestamp = int(timestamp)  # Konversi string menjadi integer
        except ValueError:
            return None  # Kembalikan None jika gagal mengonversi
    # Pastikan timestamp adalah angka (integer)
    if isinstance(timestamp, (int, float)):
        return datetime.fromtimestamp(timestamp / 1000, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    return None

def getCases(token, status_filter=None, tenantid_filter=None):
    headers = {"Authorization": "Bearer " + token, 'content-type': 'application/json'}
    
    # Zona waktu UTC+7
    tz = pytz.timezone('Asia/Jakarta')

    # Mendapatkan waktu saat ini di UTC+7
    now = datetime.now(tz)

    # Menghitung waktu mulai hari ini (00:00 UTC+7) dan waktu saat ini
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = now  # Waktu saat ini

    # Mengonversi ke format ISO untuk Elasticsearch
    start_of_day_str = start_of_day.isoformat()
    end_of_day_str = end_of_day.isoformat()

    # Membuat query untuk filter berdasarkan event_status, tenantid, dan rentang waktu
    query = {
        "size": 1000,  # Membatasi jumlah data yang diambil (maksimum 1000)
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

    # Menambahkan filter untuk rentang waktu hari ini
    query["query"]["bool"]["must"].append({
        "range": {
            "timestamp": {
                "gte": start_of_day_str,
                "lte": end_of_day_str,
                "format": "strict_date_time"
            }
        }
    })

    # Mengirimkan permintaan dengan query yang telah difilter
    url = urlunparse(("https", HOST, "/connect/api/data/aella-ser-*/_search", "", "", ""))
    res = requests.get(url, headers=headers, json=query, verify=False)
    
    # Memeriksa apakah response status OK
    if res.status_code != 200:
        print("Error: API response error.")
        return []

    # Mendapatkan data dari response JSON
    data = res.json()

    # Memeriksa apakah ada hits dan jika ada, tampilkan data
    if 'hits' in data and 'hits' in data['hits']:
        total_hits = data['hits']['total']['value']
        print(f"Total hits: {total_hits}")
        if total_hits == 0:
            print("Tidak ada data ditemukan")
            return []
        
        # Mengelompokkan alert berdasarkan "Alert Type"
        alert_groups = {}

        for case in data['hits']['hits']:
            # Ambil data dari _source untuk keperluan output
            alert_type = case["_source"].get("xdr_event", {}).get("display_name", "Unknown Alert Type")

            # Menambahkan alert type ke dalam kelompok
            if alert_type not in alert_groups:
                alert_groups[alert_type] = 0
            alert_groups[alert_type] += 1

        return alert_groups

    return []  # Jika tidak ada hits, kembalikan list kosong

if __name__ == "__main__":
    # Step 2: Use getAccessToken with supplied credentials to generate JWT
    jwt = getAccessToken(userid, refresh_token)

    # Step 3: Mengambil status dari argumen baris perintah (sys.argv)
    if len(sys.argv) < 2:
        print("masukkan status nya apa bussett")
        sys.exit(1)

    status = sys.argv[1]  # Ambil status yang diterima dari perintah (misalnya "Closed")
    tenantid = "<tenentID or custID>"  # Ganti dengan tenantid yang sesuai jika perlu

    # Memanggil fungsi getCases dengan filter status, tenantid, dan waktu hari ini
    alert_groups = getCases(jwt, status_filter=status, tenantid_filter=tenantid)

    # Batasi jumlah data yang ditampilkan hanya 8 data pertama
    if alert_groups:
        print(f"Jumlah Alert = {sum(alert_groups.values())}\n")  # Menampilkan jumlah total alert

        # Menampilkan alert type dan jumlah masing-masing
        index = 1
        for alert_type, count in alert_groups.items():
            print(f"{index}. {alert_type} : {count}")
#            print("-------------------------------------")
            index += 1
    else:
        print("Tidak ada data dalam filter yang anda masukkan")
