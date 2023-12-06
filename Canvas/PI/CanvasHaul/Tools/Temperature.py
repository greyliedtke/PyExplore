# function to get weather in San francisco

import requests

# Define the API key, base URL, and city name
api_key = "3b3d6d2fe58311968a2bb7e862f5af7e"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "San Francisco"
units = 'imperial'
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=" + units

def get_temperature():
    response = requests.get(complete_url)
    data = response.json()
    # print(data)
    if data["cod"] != "404":
        temp_f = data["main"]["temp"]
        temp_f = round(temp_f, 0)
        int_tempf = int(temp_f)
        print(f"Temp: {int_tempf}")
        return int_tempf
    else:
        return 0