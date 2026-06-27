import requests
from difflib import SequenceMatcher

city_name = input('enter the name of your city: ')
print(f'you entered:{city_name}')


city_wttr = f'https://wttr.in/{city_name}?format=j1'
try:
    req_get = requests.get(city_wttr)
    weather_data = req_get.json()
    area_name = weather_data['nearest_area'][0]['areaName'][0]['value']
    ratio = SequenceMatcher(None, city_name, area_name).ratio()
    print(ratio)
    if ratio < 0.5:
        print('city not found!')
    else:
        
        current_wttr = weather_data['current_condition']
        current = current_wttr[0]
        print(f'Weather in {city_name}')
        print(f'condition: {current['weatherDesc'][0]['value']}')
        print(f'Temperature: {current['temp_C']} feels like : {current['FeelsLikeC']}')
        print(f'humidity: {current['humidity']}%')
        print(f'wind speed: {current['windspeedKmph']}')
except requests.exceptions.RequestException as e:
    print('something went wrong!')
    
    










