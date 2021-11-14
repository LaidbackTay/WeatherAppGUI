import tkinter as tk
import tkinter.font as fnt
import requests
from PIL import Image, ImageTk

root = tk.Tk()

HEIGHT = 500
WIDTH = 600

def format_response(weather):
    try:
        loca = f'{weather["name"]}, {weather["sys"]["country"]}'
        desc = weather['weather'][0]['description']
        temps = f'{weather["main"]["temp"]}\nFeels Like (°F): {weather["main"]["feels_like"]}'

        final_str = f'Location: {str(loca)}\nConditions: {str(desc)}\nTemperature (°F): {str(temps)}'

    except:
        final_str = 'There was a problem retrieving that information'

    return final_str

def get_weather(city):
    weather_key = '8f0b2efb69946b68f9991eef41f00859'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q':city, 'units': 'imperial'}
    res = requests.get(url, params=params)
    weather = res.json()

    label['text'] = format_response(weather)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
bg_image = tk.PhotoImage(file = "Assets/nature.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

canvas.pack()

entry_frame = tk.Frame(root, bg='#80c1ff')
entry_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

body_frame = tk.Frame(root, bg='#80c1ff', bd=10)
body_frame.place(relx=0.5, rely=0.25, relwidth=.75, relheight=0.60, anchor='n')

entry = tk.Entry(entry_frame, bg='white', font=fnt.Font(family='Courier', size=15, weight='bold'))
entry.place(relx=0.015, rely=0.14,relwidth=0.67, relheight=0.75)

weather_button = tk.Button(entry_frame, text='Get Weather', font=fnt.Font(family='Courier', size=13), command=lambda: get_weather(entry.get()))
weather_button.place(relx=0.71, rely=0.14, relwidth=0.27, relheight=0.75)

label = tk.Label(body_frame, bg='white', font=fnt.Font(family='Courier', size=18, weight='bold'), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()