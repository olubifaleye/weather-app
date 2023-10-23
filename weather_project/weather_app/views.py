# Imports
from datetime import datetime

import requests
from django.shortcuts import render

# Create your views here.

# Index viewport 
def index(request):

    # load the API_key
    API_KEY = open("API_KEY", "r").read()

    # Current weather URL to target
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

    # Forecasrt weather URL to target
    forecast_weather_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"

    # Check if request is GET or POST
    if request.method == "POST":
        
        # post locations (city/country etc)
        city1 = request.POST['city1']

        # Make city2 optional
        # try to POST get, if it doesnt exist, pass
        city2 = request.POST.get('city2', None)


        # Fetch information from the forecast and render into the data template
        weather_data1, daily_forecasts1 = fetch_weather_and_forecast(city1, API_KEY, current_weather_url, forecast_weather_url)

        # Check if there is a second city
        if city2:

            # Create fetch variables for forecast information
            weather_data2, daily_forecasts2 = fetch_weather_and_forecast(city2, API_KEY, current_weather_url, forecast_weather_url)
        else:
            # If not set to None
            weather_data2, daily_forecasts2 = None, None

        # Context dictionary
        context = {
            "weather_data1": weather_data1,
            "daily_forecasts1": daily_forecasts1,
            "weather_data2": weather_data2,
            "daily_forecasts2": daily_forecasts2,
        }

        # render a html template
        return render(request, "weather_app/index.html", context)

    else:
        # render a html template
        return render(request, "weather_app/index.html")
    


# Fetch weather and forecast
def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_weather_url):

    # send GET request to the current forecast url 
    # take city and API Key as format in JSON
    response = requests.get(current_weather_url.format(city, api_key)).json()

    # Extract Long and Lat Coordinates
    lat = response['coord']['lat']
    lon = response['coord']['lon']

    # Extract Long and Lat Coordinates from forecast weather as format in JSON
    forecast_response = requests.get(forecast_weather_url.format(lat,lon,api_key)).json()

    # Store into a dictionary to pass into template
    # for temperature get response temperature value (in Kelvin) and minus 273.15 and round to 2 dp
    weather_data = {
        "city": city,
        "temperature": str(round(response['main']['temp'] - 273.15, 2)) + "°C",
        "description": response['weather'][0]['description'],
        "humidity": response['main']['humidity'],
        "wind_speed": response['wind']['speed'],
        "icon": response['weather'][0]['icon'] 
    }

    # Daily forecasts list
    daily_forecasts = []

    # Look at 5 days
    for data in forecast_response['daily'][:5]:

        # Get timestamp for the day of the forecast
        timestamp = data['dt']
        date_time = datetime.fromtimestamp(timestamp)

        # append day data to daily_forecasts list as dictionary inputs
        daily_forecasts.append({
            "day": date_time.strftime("%A"),
            "min_temp": round(data['temp']['min'] - 273.15, 2),
            "max_temp": round(data['temp']['max'] - 273.15, 2),
            "humidity": response['main']['humidity'],
            "wind_speed": response['wind']['speed'],            
            "description": data['weather'][0]['description'],
            "icon": data['weather'][0]['icon'] 
        })

    # return weather data and daily forecast data collected
    return weather_data, daily_forecasts