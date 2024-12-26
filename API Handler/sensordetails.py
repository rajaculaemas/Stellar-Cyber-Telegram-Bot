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
    print(res.status_code)
    return res.json()["access_token"]

def getSensors(token):
    headers = {"Authorization": "Bearer " + token}
    url = urlunparse(("https", HOST, "/connect/api/v1/data_sensors?limit=1", "", "", ""))
    res = requests.get(url, headers=headers, verify=False)
    print(res.status_code)
    return res.json()

def format_timestamp(timestamp):
    # Mengonversi timestamp dari milidetik ke format yang dapat dibaca
    return datetime.datetime.fromtimestamp(timestamp / 1000, tz=datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

def format_sensor_output(sensors_data):
    if 'sensors' in sensors_data and isinstance(sensors_data['sensors'], list):
        for sensor in sensors_data['sensors']:
            if isinstance(sensor, dict):  # Pastikan sensor adalah dictionary
#                print(f"id\t\t\t: {sensor.get('_id', 'N/A')}")
#                print(f"aggregator_list\t\t: {sensor.get('aggregator_list', 'none')}")
#                print("Additional Config")
                
                # Mengonversi string JSON menjadi dictionary
                additional_config = json.loads(sensor.get('additional_config', '{}'))
#                print(f"aws_mirror\t\t: {additional_config.get('aws_mirror', {})}")
#                print(f"tls_syslog\t\t: {additional_config.get('tls_syslog', {})}")
                
                # Ambil dan cetak data lainnya
#                for key in ['cpu_usage', 'tenantid', 'cust_name', 'disk_usage']:
#                    print(f"{key}\t\t: {sensor.get(key, 'N/A')}")
                
#                print("Service Status")
                
                # Ambil svc_status
                svc_status = json.loads(sensor.get('service_status', '{}')).get('svc_status', {})
#                for key, value in svc_status.items():
#                    print(f"{key}\t\t\t: {value}")
                
                # Ambil data tambahan
                for key in ['nat_ip_address', 'sensor_id', 'hostname', 'internal_sensor_id', 'local_ip_address', 
                            'license', 'mem_usage', 'mode', 'module_version', 'sw_version', 'timezone', 
                            'last_stats_time', 'cm_worker_id', 'message', 'need_upgrade']:
                    if key == 'last_stats_time':
                        print(f"{key}\t\t: {format_timestamp(sensor.get(key, 0))}")
                    else:
                        print(f"{key}\t\t: {sensor.get(key, 'N/A')}")
                
                print("\n" + "="*50 + "\n")  # Pembatas antar sensor
            else:
                print(f"Unexpected sensor format: {sensor}")  # Debugging untuk format yang tidak terduga
    else:
        print("Data sensor tidak dalam format yang diharapkan. Data yang diterima:")
        print(sensors_data)  # Tampilkan data untuk debugging

if __name__ == "__main__":
    # Step 2: Use getAccessToken with supplied credentials to generate JWT
    jwt = getAccessToken(userid, refresh_token)

    # Step 3: use JWT token to call public API
    sensors = getSensors(jwt)
    print("------------ call result of /connect/api/v1/sensors -------------")
    
    # Format dan tampilkan output sensor
    format_sensor_output(sensors)
    
    print("------------ end api results -------------")
