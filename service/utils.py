import aiohttp
import asyncio
from datetime import datetime

API_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY = "e4e4bcbc7f952057784142e5081ae197"


def convert_unix_to_time(unix_time):
    time = datetime.fromtimestamp(unix_time)
    return time.strftime("%d %B, %H:%M")


async def get_weather(city_name):
    async with aiohttp.ClientSession() as session:
         async with session.get(API_URL+f"?q={city_name}&appid={WEATHER_API_KEY}") as r:
            data = await r.json()
            weather_data = {
                "temp": round(data ["main"] ["temp"] - 273), # Превращаем в цельсии.
                "feels_like": round(data["main"] ["feels_like"] - 273),
                "pressure": data["main"] ["pressure"],
                "humidity": data["main"] ["humidity"],
                "wind_speed": data["wind"] ["speed"],
                "city_time": convert_unix_to_time(data["dt"]),
                "sunset": convert_unix_to_time(data["sys"] ["sunset"]),
                "sunrise": convert_unix_to_time(data["sys"] ["sunrise"])
            }
            print(weather_data)
            return weather_data

