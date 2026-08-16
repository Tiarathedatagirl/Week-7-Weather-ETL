import requests
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
cities = ["Lagos", "Abuja", "London"]
url = "https://api.openweathermap.org/data/2.5/weather"

weather_data = []

for city in cities:
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()
    weather_data.append(data)

print(weather_data)
weather_list = []

for data in weather_data:
    weather_list.append({
        "City": data["name"],
        "Temperature": data["main"]["temp"],
        "Humidity": data["main"]["humidity"],
        "Weather Condition": data["weather"][0]["description"],
        "Wind Speed": data["wind"]["speed"],
        "Date and Time": data["dt"]
    })

df = pd.DataFrame(weather_list)

print(df)
df["Date and Time"] = pd.to_datetime(df["Date and Time"], unit="s")

print(df)
df.to_csv("weather_data.csv", index=False)
print("Temperature Comparison:")
print(df[["City", "Temperature"]])
print("Highest Humidity:")
print(df.loc[df["Humidity"].idxmax(), ["City", "Humidity"]])
print("Weather Conditions:")
print(df[["City", "Weather Condition"]])