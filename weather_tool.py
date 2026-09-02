import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

print(API_KEY)

def get_weather(city: str):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    weather_data = response.json()

    #print(weather_data)

    return {
        "city": weather_data["name"],
        "temperature": weather_data["main"]["temp"],
        "feels_like": weather_data["main"]["feels_like"],
        "humidity": weather_data["main"]["humidity"],
        "condition": weather_data["weather"][0]["main"],
        "description": weather_data["weather"][0]["description"],
        "wind_speed": weather_data["wind"]["speed"]
    }
