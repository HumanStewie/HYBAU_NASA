# This is not done. Currently data needs to be properly formatted
# Also forecast duration need to be changed
import requests

def get_weather(lat, lon):
    base = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,relative_humidity_2m,precipitation",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto",
        "forecast_days": 1
    }
    recall = requests.get(base, params=params)
    recall.raise_for_status()
    return recall.json()

data = get_weather(21.0278, 105.8342)
print(data)

