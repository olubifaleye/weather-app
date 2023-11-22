# Weather Application
This is a Weather Application built with Python Django and JavaScript. It allows users to check the current weather conditions for a specific location. The application utilizes the OpenWeatherMap API to fetch weather data and provides a user-friendly interface to display this information.

## Features

- Weather Information: Users can enter a City to retrieve thier current weather data, including the City's name, temperature, humidity, wind speed, short weather description and 5-day forecast.
- Compare Weather Information: Users can compare weather data between 2 different cities.

## Installation

### Prerequisites
- Python 3.7+
- Django
- JavaScript (for front-end)
- OpenWeatherMap API Key [Get one here](https://openweathermap.org/)
- You must create a file in weather_project directory called "API_KEY". This is were you will store your own OpenWeatherMap API Key

## Usage

1. Open the application in your web browser.
2. Enter a City name in the first search bar, the second search bar is optional.
3. Click the "Compare Weather" button to fetch and display the current weather information for the specified location(s).

# Acknowledgments

- The Weather Application is built using Django and JavaScript.
- Weather data is provided by the OpenWeatherMap API.

# Running Django Project

 - Clone the repository
 - navigate to the projects directory
 - install the projects dependancies using:

 ```pip install -r requirements.txt```

- Then to start the development server, run the following the command:

  ```python manage.py runserver```

  The development server will start, and you can access the app in your web browser at (http://127.0.0.1:8000/).


