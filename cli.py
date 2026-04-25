def display_weather(city, country, weather_data, units):
    daily = weather_data["daily"]

    unit_symbol = "°C" if units == "metric" else "°F"

    print(f"\n🌍 Weather Forecast for {city}, {country}")
    print("=" * 40)

    for i in range(len(daily["time"])):
        date = daily["time"][i]
        max_temp = daily["temperature_2m_max"][i]
        min_temp = daily["temperature_2m_min"][i]

        print(f"{date} | Max: {max_temp}{unit_symbol} | Min: {min_temp}{unit_symbol}")

    print("=" * 40)