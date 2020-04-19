import requests
from tkinter import *

root = Tk()
city = Entry(root, text='city')
city.pack()
label = Label(root, text='').pack()
def submit(city):
    global label
    weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3';url = 'https://api.openweathermap.org/data/2.5/weather';params = {'APPID': weather_key, 'q': city, 'units': 'imperial'};response = requests.get(url, params=params);weather = response.json()
    try:
        tem = weather['main']['temp']

        x = f' Temperature (°F): {tem}'
    except:
        x = f'no city name called {city.get()}'

    label = Label(root, text=x).pack()


button = Button(root, text='done', command=lambda: submit(city.get())).pack()
mainloop()
