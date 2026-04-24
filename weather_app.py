import tkinter as tk
import requests

def get_weather(city_name, api_key, units):
    # The base URL for the OpenWeatherMap API
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Parameters we will send to the API
    params = {
        "q": city_name,
        "appid": api_key,
        "units": units  # Use "metric" for Celsius, "imperial" for Fahrenheit
    }

    try:
        # Sending a GET request to the API
        response = requests.get(base_url, params=params)
        
        # Check if the city was found and request was successful
        if response.status_code == 200:
            # Convert the JSON response into a Python dictionary
            data = response.json()
            
            # Extracting specific data from the dictionary
            city = data['name']
            country = data['sys']['country']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            unit_symbol = "°C" if units == "metric" else "°F"
            desc = data['weather'][0]['description']
            result = f"{city}, {country}\nTemp: {temp}{unit_symbol}\nCondition: {desc.title()}"
            result_label.config(text=result)

            # Displaying the results in a nice format
            print("\n" + "="*30)
            print(f"🌍 Weather in {city}, {country}:")
            print("="*30)
            print(f"🌡️ Temperature: {temp}{unit_symbol} (Feels like {feels_like}{unit_symbol})")
            print(f"☁️  Condition:   {description.title()}")
            print(f"💧 Humidity:    {humidity}%")
            print(f"💨 Wind Speed:  {wind_speed} m/s")
            print("="*30 + "\n")

            with open("weather_history.txt", "a") as file:
            
                file.write(f"{city}, {country} | Temp: {temp} | Feels Like: {feels_like} | Condition: {description} | Humidity: {humidity} | Wind: {wind_speed}\n")
            
        elif response.status_code == 404:
            print(f"\n❌ Error: City '{city_name}' not found. Please check the spelling.\n")
        elif response.status_code == 401:
            print("\n❌ Error: Invalid API Key. It might take a few minutes for a new key to activate.\n")
        else:
            print(f"\n❌ Error: Failed to get weather data. Status code: {response.status_code}\n")
            result_label.config(text="City not found")
    # This handles network errors
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Network Error: Please check your internet connection.\n")
        result_label.config(text="Network error")


def main():
    print("🌤️  Welcome to the Python Weather App! 🌤️")
    
    # YOUR API KEY IS RIGHT HERE:
    api_key = "f55cc56faf381e75dbc05c8938fdcefb" 

    unit_choice = input("Choose unit - Celsius (C) or Fahrenheit (F): ").strip().lower()

    if unit_choice == "f":
        units = "imperial"
    elif unit_choice == "c":
        units = "metric"
    else:
        print("Invalid choice. Defaulting to Celsius.")
        units = "metric"

        city = input("Enter a city name (or type 'quit' to exit): ").strip()

        get_weather(city, api_key, units)

# This ensures the code only runs if the script is executed directly
if __name__ == "__main__":
    main()

    # UI Setup
app = tk.Tk()
app.title("Weather App")
app.geometry("300x250")
api_key = "f55cc56faf381e75dbc05c8938fdcefb" 

tk.Label(app, text="Enter City").pack(pady=10)

city_entry = tk.Entry(app)
city_entry.pack()
unit_var = tk.StringVar(value="metric")  # default Celsius

tk.Radiobutton(app, text="Celsius (°C)", variable=unit_var, value="metric").pack()
tk.Radiobutton(app, text="Fahrenheit (°F)", variable=unit_var, value="imperial").pack()
tk.Button(app, text="Get Weather", command=lambda: get_weather(city_entry.get(), api_key, "metric")).pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

app.mainloop()