from ambient_api.ambientapi import AmbientAPI
import time

def recieve_data(api):
    station = api.get_devices()[0]
    data = station.last_data
    time.sleep(1)
    return data