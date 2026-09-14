import os
import requests
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv

## API Doc: https://docs.greenstream.cloud/

load_dotenv()

API_KEY = os.getenv("GREAN_STREAM_API_KEY")
BASE_URL = "https://api.greenstream.cloud"

headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

def get_devicelist():
    response = requests.get(f"{BASE_URL}/sites", headers=headers)
    sites = response.json()
    device_list = []
    for site in sites:
        device = site.get('device')
        device_list.append(device)
    device_list.sort()
    print(device_list)

def get_deviceid():
    response = requests.get(f"{BASE_URL}/sites", headers=headers)
    sites = response.json()
    id_list = []
    for site in sites:
        device = site.get('id')
        id_list.append(device)
    id_list.sort()
    print(id_list)

def get_device_id_hash():
    response = requests.get(f"{BASE_URL}/sites", headers=headers)
    sites = response.json()
    device_id_dict = {}
    for site in sites:
        device = site.get('device')
        id = site.get('id')
        device_id_dict[id] = device
    sorted_dict = dict(sorted(device_id_dict.items(), key = lambda item: item[1]))
    print(sorted_dict)

def get_devices():
    response = requests.get(f"{BASE_URL}/devices", headers=headers)
    devices = response.json()
    for device in devices:
        device = device.get('name')
        print(device)

def get_readings(id):

    hourago = datetime.now() - timedelta(hours=1)

    start = int(hourago.timestamp())
    end = int(datetime.now().timestamp())

    params = {
        "id": id,
        "start": start,
        "end": end
    }

    response = requests.get(f"{BASE_URL}/site/messages", headers=headers, params=params)
    messages = response.json()
    stage_list = []
    for message in messages:
        stage = message.get('stage')
        stage_list.append(stage)
    
    print(stage_list)


get_readings("867c5ecb-6b7b-4d78-8c11-933d71704df0")