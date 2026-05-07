import requests
import os
from dotenv import load_dotenv
from tkinter import messagebox
import tkinter as tk

load_dotenv()

root = tk.Tk()
root.withdraw()

# Windows color support
os.system('')
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = '\033[31m'
RESET = "\033[0m"

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY") #---the api key
    print(f"DEBUG: Key found: {api_key}")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try: 
        response = requests.get(url)
        data = response.json()
        #print(data)

        if response.status_code == 200:
            #Extracting the data
            #city_name = data['name']
            temp = data ['main']['temp']
            desc = data ['weather'][0] ['description']

            #------------POP UP DISPLAY ----------------

            weather_info = f"City: {city.capitalize()}\nTemperature: {temp} °C\nConditions: {desc.capitalize()} \n Wind Speed: {data ["wind"]["speed"]} m/s"
            messagebox.showinfo("Weather Report: ", weather_info)

           # humidity = data ['main']['humidity']
            # wind = data['wind']['speed']
            #print("-" * 30)
            #print(f"\n{CYAN}WEATHER REPORT:  {city_name.upper()}{RESET}")
            #print("-" * 30)
            #print(f"Temperature: {YELLOW}{temp} °C {RESET}")
            #print(f"Conditions: {desc.capitalize()}") 

            if "rain" in desc:
                #print(f"{RED} Bring an umbrella!! {RESET}")
                messagebox.showwarning("Weather Alert!, It's raining! Bring your umbrella!")
            elif "clear" in desc:
                #print(f"{YELLOW} Don't forget your shades!!{RESET}")
                messagebox.showinfo("Weather Alert!", "It's a clear day! Don't forget your shades!")
            elif "clouds" in desc:
                #print("It is a bit gloomy today")
                messagebox.showinfo("Weather Alert!", "It's a bit gloomy today.")
            else:
                #print("Your weather is okay, enjoy!")
                messagebox.showinfo("Weather Alert!", "Your weather is okay, enjoy!")
                
            ##print(f"Wind Speed: {wind} m/s")
            ##print(f"Humidity: {humidity}%")
            ##print("-" * 30)
        else:
            ##print(f"City not found. (Error {response.status_code})")
            messagebox.showerror("Error", f"City not found. (Error {response.status_code})")
    
    except Exception as e:
        ##print("Could not connect to the weather service.")
        messagebox.showerror("Error", "Could not connect to the weather service.")

if __name__ == "__main__":
    print("Weather App is running! Check your pop-ups!!!")
    while True:
        city_input = input("\n Enter city name (or 'exit' to quit): ")
        if city_input.lower() == 'exit':
            break
        get_weather(city_input)