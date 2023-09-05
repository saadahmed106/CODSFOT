import tkinter as tk
import requests

def get_weather():
    api_key = "YOUR_API_KEY_HERE"
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_info = data["main"]
        temperature = weather_info["temp"]
        humidity = weather_info["humidity"]
        weather_description = data["weather"][0]["description"]
        result_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWeather: {weather_description}")
    else:
        result_label.config(text="City not found!")

# Create the main window
root = tk.Tk()
root.title("Weather Forecast")

# Create and place GUI elements
city_label = tk.Label(root, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
