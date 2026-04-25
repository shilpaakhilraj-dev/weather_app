from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

# reuse your existing modules
from api import get_weather as fetch_weather
from geocode import get_coordinates
from cli import display_weather
from utils import parse_args

app = FastAPI()

# CORS (needed for Angular)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API endpoint
@app.get("/weather")
def weather_api(city: str = Query(...), units: str = "metric"):
    try:
        coords = get_coordinates(city)

        if not coords:
            return {"error": "City not found"}

        lat, lon, name, country = coords

        weather_data = fetch_weather(lat, lon, units)

        return {
            "city": name,
            "country": country,
            "forecast": weather_data["daily"]
        }

    except Exception as e:
        return {"error": str(e)}


# CLI still works (unchanged logic)
def main():
    args = parse_args()

    try:
        if not args.city and not (args.lat and args.lon):
            print("🌤️ Welcome to Weather CLI App")

            choice = input("Search by City (C) or Coordinates (L)? ").strip().lower()

            if choice == "c":
                city_input = input("Enter city name: ").strip()
                lat, lon, city, country = get_coordinates(city_input)

            elif choice == "l":
                lat = float(input("Enter latitude: "))
                lon = float(input("Enter longitude: "))
                city, country = "Custom Location", ""

            else:
                print("Invalid choice")
                return

            unit_choice = input("Choose unit - Celsius (C) or Fahrenheit (F): ").strip().lower()
            units = "imperial" if unit_choice == "f" else "metric"

        else:
            units = args.units

            if args.city:
                lat, lon, city, country = get_coordinates(args.city)
            else:
                lat, lon = args.lat, args.lon
                city, country = "Custom Location", ""

        weather_data = fetch_weather(lat, lon, units)
        display_weather(city, country, weather_data, units)

    except Exception as e:
        print(f"❌ Error: {e}")


# Important: DO NOT auto-run CLI when running API
if __name__ == "__main__":
    main()