#!/usr/bin/python3

import requests
import base64
import json
from urllib.parse import urlunparse
from datetime import datetime, timedelta, timezone

# Disable SSL warnings kalo pake SSL tinggal dipagerin ghoib
requests.packages.urllib3.disable_warnings()

# Step 1
# Tambahkan IP/hostname, userid, dan refresh token dari GUI stellar cyber anda
HOST = "<your stellar cyber IP/domain>"
userid = "<stellar cyber user id>"
refresh_token = "<stellar cyber refresh token>"

# Fungsi untuk mendapatkan akses token, ini bawaan dari doc stellar (JWT)
def getAccessToken(userid, refresh_token):
    auth = base64.b64encode(bytes(userid + ":" + refresh_token, "utf-8")).decode("utf-8")
    headers = {
        "Authorization": "Basic " + auth,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    url = urlunparse(("https", HOST, "/connect/api/v1/access_token", "", "", ""))
    res = requests.post(url, headers=headers, verify=False)
    
    # Check if the response is successful
    if res.status_code == 200:
        return res.json()["access_token"]
    else:
        print(f"Failed to get access token: {res.status_code} {res.text}")
        return None

# Function to get data from the API (connector, sensor, log-source, log-type)
def getData(token, endpoint, start_time, end_time):
    headers = {"Authorization": "Bearer " + token}
    
    # Modify the URL and query parameters if needed
    url = urlunparse(("https", HOST, endpoint, "", f"start_time={start_time}&end_time={end_time}", ""))
    
#    print(f"Requesting: {url}")
    
    res = requests.get(url, headers=headers, verify=False)
    
    # Check if the response is successful
    if res.status_code == 200:
        return res.json().get("data", [])
    else:
        print(f"Failed to fetch data from {endpoint}: {res.status_code} {res.text}")
        return []

# Function to convert bytes to MB and round to 2 decimal places
def bytes_to_mb(byte_value):
    return round(byte_value / (1024 * 1024 * 1024), 2) if byte_value else 0.0

# Function to calculate the total ingestion for a specific day
def calculate_total_ingestion(data):
    total = sum(item["total_ingestion"] for item in data)
    return bytes_to_mb(total)

# Function to format and display the data
def display_data(date, connectors, sensors, log_sources, log_types):
    print(f"Tanggal: {date}")
    
    # Display Connector Ingestion
    connector_total = calculate_total_ingestion(connectors)
    print(f"1. Connector Ingestion (Jumlah: {connector_total} GB)")
#    for connector in connectors:
#        print(f"- Nama connector: {connector['entry_identifier']}")
#        print(f"  Total Ingestion: {bytes_to_mb(connector['total_ingestion'])} MB")
#        print("="*90)

    # Display Sensor Ingestion
    sensor_total = calculate_total_ingestion(sensors)
    print(f"2. Sensor Ingestion (Jumlah: {sensor_total} GB)")
#    for sensor in sensors:
#        print(f"- Nama sensor: {sensor['entry_identifier']}")
#        print(f"  Total Ingestion: {bytes_to_mb(sensor['total_ingestion'])} MB")
#        print("="*90)

    # Display Log Source Ingestion
    log_source_total = calculate_total_ingestion(log_sources)
    print(f"3. Log Source Ingestion (Jumlah: {log_source_total} GB)")
#    for log_source in log_sources:
#        print(f"- Nama Log Source: {log_source['entry_identifier']}")
#        print(f"  Total Ingestion: {bytes_to_mb(log_source['total_ingestion'])} MB")
#        print("="*90)

    # Display Log Type Ingestion
    log_type_total = calculate_total_ingestion(log_types)
    print(f"4. Log Type Ingestion (Jumlah: {log_type_total} GB)")
    print("="*40)
#    for log_type in log_types:
#        print(f"- Nama Log Type: {log_type['entry_identifier']}")
#        print(f"  Total Ingestion: {bytes_to_mb(log_type['total_ingestion'])} MB")
#        print("="*90)

# Main function to get data for the last 5 days
def main():
    jwt = getAccessToken(userid, refresh_token)
    
    # Check if the token is valid
    if not jwt:
        return

    # Get the current date and the 5 previous days
    today = datetime.now(timezone.utc) - timedelta(days=1)
    dates = [today - timedelta(days=i) for i in range(5)]
    
    # Sort the dates from the earliest to the latest (ascending)
    sorted_dates = sorted(dates)
    
    # Loop through each sorted date to fetch and display the data
    for date in sorted_dates:
        # Format start and end time with no 'Z' and use the correct format
        start_time = date.strftime("%Y-%m-%dT00:00:00")
        end_time = date.strftime("%Y-%m-%dT20:59:59")
        
#        print(f"Fetching data for {start_time} to {end_time}...")

        # Fetch data from all 4 endpoints for each day
        connectors = getData(jwt, "/connect/api/v1/ingestion-stats/connector", start_time, end_time)
        sensors = getData(jwt, "/connect/api/v1/ingestion-stats/sensor", start_time, end_time)
        log_sources = getData(jwt, "/connect/api/v1/ingestion-stats/log-source", start_time, end_time)
        log_types = getData(jwt, "/connect/api/v1/ingestion-stats/log-type", start_time, end_time)
        
        # Display the results for the current day
        display_data(date.strftime("%Y-%m-%d"), connectors, sensors, log_sources, log_types)

if __name__ == "__main__":
    main()
