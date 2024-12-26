#!/usr/bin/python3

import requests
import base64
import json
import datetime
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
#    print(res.status_code)
    return res.json()["access_token"]

def getSensors(token):
    headers = {"Authorization": "Bearer " + token}
    url = urlunparse(("https", HOST, "/connect/api/v1/data_sensors/<your sensor ID 2>", "", "", ""))
    res = requests.get(url, headers=headers, verify=False)
#    print(res.status_code)
    return res.json()

def format_timestamp(timestamp):
    # Mengonversi timestamp dari milidetik ke format yang dapat dibaca
    return datetime.datetime.fromtimestamp(timestamp / 1000, tz=datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

def format_sensor_output(sensor_data):
    if isinstance(sensor_data, dict):  # Pastikan data sensor adalah dictionary
        print("=====================================")
        print(f"sensor_id: {sensor_data.get('sensor_id', 'N/A')}")
#        print(f"aggregator_list: {sensor_data.get('aggregator_list', 'none')}")
#        print(f"tenantid: {sensor_data.get('tenantid', 'N/A')}")
        print(f"cust_name: {sensor_data.get('cust_name', 'N/A')}")
        
        # Format nilai disk_usage dan mem_usage menjadi satu desimal
        print(f"disk_usage : {sensor_data.get('disk_usage', 'N/A'):.1f}")
        print(f"nat_ip_address: {sensor_data.get('nat_ip_address', 'N/A')}")
        print(f"hostname: {sensor_data.get('hostname', 'N/A')}")
        print(f"local_ip_address: {sensor_data.get('local_ip_address', 'N/A')}")
#        print(f"mem_usage: {sensor_data.get('mem_usage', 'N/A'):.1f}")
        
        print(f"sw_version: {sensor_data.get('sw_version', 'N/A')}")
        
        # Format waktu terakhir statistik
        last_stats_time = sensor_data.get('last_stats_time', 0)
        print(f"last_stats_time: {format_timestamp(last_stats_time)}")
        
        print(f"need_upgrade: {sensor_data.get('need_upgrade', 'N/A')}")
        print("=====================================")
    else:
        print("Data sensor tidak dalam format yang diharapkan. Data yang diterima:")
        print(sensor_data)  # Tampilkan data untuk debugging

if __name__ == "__main__":
    # Step 2: Use getAccessToken with supplied credentials to generate JWT
    jwt = getAccessToken(userid, refresh_token)

    # Step 3: use JWT token to call public API
    sensors = getSensors(jwt)
    
    # Format dan tampilkan output sensor
    format_sensor_output(sensors)
