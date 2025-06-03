import os
import time
import requests
import csv
from datetime import datetime

ESP_SENSORS = [
    {"ssid": "ESP_SoilSensor_1", "ip": "192.168.4.1"},
    {"ssid": "ESP_SoilSensor_2", "ip": "192.168.4.1"}
]
homewifi="Airtel_Kishore Wifi"
def connect_to_esp(ssid):
    print(f"\nConnecting to {ssid}...")
    os.system(f"nmcli device wifi connect {ssid} password 12345678")
    time.sleep(5) 

def get_soil_moisture(ip):
    url = f"http://{ip}/"
    try:
        response = requests.get(url, timeout=20)
        if response.status_code == 200:
            print(f"Soil Moisture from {ip}: {response.text}")
            return response.text
    except Exception as e:
        print(f"Failed to get data from {ip}: {e}")
    return None

def log_data_to_csv(data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("data.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([data, timestamp])


if not os.path.exists("data.csv"):
    with open("data.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Moisture Value", "Timestamp"])

while True:
    for esp in ESP_SENSORS:
        connect_to_esp(esp["ssid"])
        moisture = get_soil_moisture(esp["ip"])
        os.system("nmcli device disconnect wlan0")
        print(f"Collected data: {moisture}")
        if moisture:
            log_data_to_csv(moisture)
    print("Waiting for 5 minutes before next cycle...")
    time.sleep(5) #only 5 second is assigned, just for demonstration
