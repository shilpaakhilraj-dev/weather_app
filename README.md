# Weather App (Python CLI + FastAPI Backend)

A simple and modular **Weather Application** built using Python that supports:

* Command Line Interface (CLI)
* REST API using FastAPI
* City-based geocoding
* 7-day weather forecast (Open-Meteo API)

---

## Features

* Get weather by **city name** or **coordinates**
* Supports **Celsius (°C)** and **Fahrenheit (°F)**
* Modular architecture:

  * API handling
  * Geocoding
  * CLI rendering
* FastAPI backend for integration with frontend apps (e.g., Angular)

---

## Project Structure

```
.
├── api.py        # Fetch weather data from Open-Meteo API
├── geocode.py    # Convert city → latitude & longitude
├── cli.py        # Display weather in terminal
├── utils.py      # Argument parsing
├── main.py       # FastAPI app + CLI entry point
```

---

## Run API Server

```bash
uvicorn main:app --reload
```

Your API will be available at:

```
http://127.0.0.1:8000
```

---

## API Endpoint

### GET `/weather`

#### Query Params:

* `city` (required)
* `units` (optional: metric / imperial)

#### Example:

```
http://127.0.0.1:8000/weather?city=Chennai
```

#### Sample Response:

```json
{
  "city": "Chennai",
  "country": "India",
  "forecast": {
    "time": ["2026-04-25"],
    "temperature_2m_max": [35],
    "temperature_2m_min": [28]
  }
}
```

---

## Tech Stack

* Python
* FastAPI
* Uvicorn
* Open-Meteo API

---

## Author

**Shilpa K**
Senior Angular Developer | Python Enthusiast

---
