import requests

def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1}

    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data:
        raise ValueError("City not found")

    result = data["results"][0]
    return result["latitude"], result["longitude"], result["name"], result["country"]