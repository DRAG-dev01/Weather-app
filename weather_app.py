import tkinter as tk
import requests
from difflib import SequenceMatcher

window = tk.Tk()
window.title("Weather App")

label = tk.Label(window, text="Enter a city name in the box below!")
label.pack()
entry = tk.Entry(window)
entry.pack()


def show_city():
    city_name = entry.get()
    city_wttr = f'https://wttr.in/{city_name}?format=j1'
    try:
        req_get = requests.get(city_wttr)
        weather_data = req_get.json()
        area_name = weather_data['nearest_area'][0]['areaName'][0]['value']
        ratio = SequenceMatcher(None, city_name, area_name).ratio()
        label.config(text=ratio)
        if ratio < 0.5:
            label.config(text='city not found!')
        else:
        
            current_wttr = weather_data['current_condition']
            current = current_wttr[0]
            label.config(text= f'Weather in {city_name}\ncondition: {current['weatherDesc'][0]['value']}\nTemperature: {current['temp_C']} feels like : {current['FeelsLikeC']}\nhumidity: {current['humidity']}%\nwind speed: {current['windspeedKmph']}')
    except requests.exceptions.RequestException as e:
        label.config(text='something went wrong!')
    
    
    


button = tk.Button(window, text="click me to see weather", command=show_city)
button.pack()

window.mainloop()