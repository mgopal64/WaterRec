from ambient_api.ambientapi import AmbientAPI
import time

def receive_data():
    try:
        api = AmbientAPI(
        AMBIENT_ENDPOINT        = "https://rt.ambientweather.net/v1",
        AMBIENT_API_KEY         = "eba6cc95d6b849a59125f46c1a49581fa027a00c4643440185efdec6edbddd97",
        AMBIENT_APPLICATION_KEY = "dfdd92b6b41d40debae8600d60428f77bf5a39871ba54381883417df45d6d9ed"
    )

        station = api.get_devices()[0]
        data = station.last_data
        time.sleep(1)
        return data
    except Exception as e:
        print("Error fetching data from Ambient API:", e)
        return None
