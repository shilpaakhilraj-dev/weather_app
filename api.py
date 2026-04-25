import requests

def get_weather(lat, lon, units="metric"):
    temp_unit = "celsius" if units == "metric" else "fahrenheit"

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min,weathercode",
        "timezone": "auto",
        "temperature_unit": temp_unit
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    
    return response.json()