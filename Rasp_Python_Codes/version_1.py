import os
import time
import requests

ESP_SENSORS = [
    {"ssid": "ESP_SoilSensor_1", "ip": "192.168.4.1"},
    {"ssid": "ESP_SoilSensor_2", "ip": "192.168.4.1"}
]

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

while True:
    for esp in ESP_SENSORS:
        connect_to_esp(esp["ssid"])
        moisture = get_soil_moisture(esp["ip"])
        os.system("nmcli device disconnect wlan0") 
        print(f"Collected data: {moisture}")
    
    print("Waiting for 5 minutes before next cycle...")
    time.sleep(1) 
