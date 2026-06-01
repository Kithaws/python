import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()
def get_current_weather():
    print("**** Welcome to the Weather App ****")
    city = input("\nEnter the city name:\n")

    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"
    
   
    weather_data = requests.get(request_url).json()
    #pprint(weather_data)
    print(f'\ncurrent weather for {weather_data['name']}')
    print(f"temperature: {weather_data['main']['temp']}°C")
    print(f"feels like: {weather_data['main']['feels_like']}°c")
get_current_weather()
