#!/usr/bin/python3

import sys
import requests
import base64
from urllib.parse import urlunparse
from datetime import datetime, timedelta
import pytz

# Menonaktifkan peringatan SSL
requests.packages.urllib3.disable_warnings()

# Step 1
# Tambahkan IP/hostname, userid, dan refresh token dari GUI stellar cyber anda
HOST = "<your stellar cyber IP/domain>"
userid = "<stellar cyber user id>"
refresh_token = "<stellar cyber refresh token>"

# Fungsi untuk mendapatkan Access Token
def getAccessToken(userid, refresh_token):
    auth = base64.b64encode(bytes(userid + ":" + refresh_token, "utf-8")).decode("utf-8")
    headers = {
        "Authorization": "Basic " + auth,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    url = urlunparse(("https", HOST, "/connect/api/v1/access_token", "", "", ""))
    res = requests.post(url, headers=headers, verify=False)
    return res.json().get("access_token")

# Fungsi untuk mendapatkan rentang waktu berdasarkan shift
def get_shift_range(shift):
    tz = pytz.timezone('Asia/Jakarta')
    now = datetime.now(tz)
    
    if shift == 'shift1':  # 07:00 - 17:00
        # Shift1 berlaku untuk jam 07:00 - 17:00
        if now.hour < 7:
            # Jika sekarang masih sebelum jam 07, shift1 adalah dari jam 07 kemarin sampai jam 17 kemarin
            start_time = (now - timedelta(days=1)).replace(hour=7, minute=0, second=0, microsecond=0)
            end_time = (now - timedelta(days=1)).replace(hour=17, minute=0, second=0, microsecond=0)
        else:
            # Jika sekarang sudah lebih dari jam 07, shift1 adalah dari jam 07 hari ini sampai jam 17 hari ini
            start_time = now.replace(hour=7, minute=0, second=0, microsecond=0)
            end_time = now.replace(hour=17, minute=0, second=0, microsecond=0)
    
    elif shift == 'shift2':  # 11:00 - 21:00
        # Shift2 berlaku untuk jam 11:00 - 21:00
        if now.hour < 11:
            # Jika sekarang masih sebelum jam 11, shift2 adalah dari jam 11 kemarin sampai jam 21 kemarin
            start_time = (now - timedelta(days=1)).replace(hour=11, minute=0, second=0, microsecond=0)
            end_time = (now - timedelta(days=1)).replace(hour=21, minute=0, second=0, microsecond=0)
        else:
            # Jika sekarang sudah lebih dari jam 11, shift2 adalah dari jam 11 hari ini sampai jam 21 hari ini
            start_time = now.replace(hour=11, minute=0, second=0, microsecond=0)
            end_time = now.replace(hour=21, minute=0, second=0, microsecond=0)
    
    elif shift == 'shift3':  # 21:00 - 07:00 hari berikutnya
        # Shift3 berlaku untuk jam 21:00 hari ini sampai jam 07:00 hari berikutnya
        if now.hour < 21:
            # Jika sekarang masih sebelum jam 21, shift3 adalah dari jam 21 kemarin sampai jam 07 hari ini
            start_time = (now - timedelta(days=1)).replace(hour=21, minute=0, second=0, microsecond=0)
            end_time = now.replace(hour=7, minute=0, second=0, microsecond=0)
        else:
            # Jika sekarang sudah lebih dari jam 21, shift3 adalah dari jam 21 hari ini sampai jam 07 hari berikutnya
            start_time = now.replace(hour=21, minute=0, second=0, microsecond=0)
            end_time = (now + timedelta(days=1)).replace(hour=7, minute=0, second=0, microsecond=0)
    else:
        print(f"Shift '{shift}' tidak valid.")
        return None, None  # Jika shift tidak valid

    return start_time, end_time

# Fungsi untuk mendapatkan data kasus dari API
def getCases(token, status_filter=None, tenantid_filter=None, shift=None):
    headers = {"Authorization": "Bearer " + token, 'content-type': 'application/json'}
    
    # Mengambil rentang waktu berdasarkan shift
    start_time, end_time = get_shift_range(shift)
    if start_time is None or end_time is None:
        print(f"Shift '{shift}' tidak valid.")
        return []

    # Mengonversi waktu ke format ISO
    start_of_shift_str = start_time.isoformat()
    end_of_shift_str = end_time.isoformat()

    # Debugging: Cetak waktu mulai dan berakhir shift
    print(f"Rentang waktu {shift}: {start_of_shift_str} - {end_of_shift_str}")

    # Membuat query untuk filter berdasarkan status, tenantid, dan rentang waktu shift
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

    # Menambahkan filter untuk rentang waktu shift
    query["query"]["bool"]["must"].append({
        "range": {
            "timestamp": {
                "gte": start_of_shift_str,
                "lte": end_of_shift_str,
                "format": "strict_date_time"
            }
        }
    })

    # Mengirimkan permintaan dengan query yang telah difilter
    url = urlunparse(("https", HOST, "/connect/api/data/aella-ser-*/_search", "", "", ""))
    res = requests.get(url, headers=headers, json=query, verify=False)
    
    # Memeriksa apakah response status OK
    if res.status_code != 200:
        print(f"Error: API response error. Status Code: {res.status_code}")
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
            alert_type = case["_source"].get("xdr_event", {}).get("display_name", "Unknown Alert Type")
            if alert_type not in alert_groups:
                alert_groups[alert_type] = 0
            alert_groups[alert_type] += 1

        return alert_groups

    return []  # Jika tidak ada hits, kembalikan list kosong

if __name__ == "__main__":
    # Step 2: Gunakan getAccessToken dengan kredensial yang disediakan untuk menghasilkan JWT
    jwt = getAccessToken(userid, refresh_token)

    # Step 3: Mengambil status dan shift dari argumen baris perintah (sys.argv)
    if len(sys.argv) < 3:
        print("Masukkan status dan shift yang valid.")
        sys.exit(1)

    status = sys.argv[1]  # Status yang diterima dari perintah (misalnya "Closed")
    shift = sys.argv[2].lower()  # Shift yang diterima dari perintah (misalnya "shift3")

    tenantid = "<tenentID or custID>"  # Ganti dengan tenantid yang sesuai jika perlu

    # Memanggil fungsi getCases dengan filter status, tenantid, dan waktu shift
    alert_groups = getCases(jwt, status_filter=status, tenantid_filter=tenantid, shift=shift)

    # Batasi jumlah data yang ditampilkan hanya 8 data pertama
    if alert_groups:
        print(f"Jumlah Alert = {sum(alert_groups.values())}\n")
        index = 1
        for alert_type, count in alert_groups.items():
            print(f"{index}. {alert_type} : {count}")
            index += 1
    else:
        print("Tidak ada data dalam filter yang anda masukkan")
