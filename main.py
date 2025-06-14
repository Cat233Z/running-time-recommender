import requests
import datetime
from recommender import get_best_times
from recommender import get_best_times, plot_scores_matplotlib

API_KEY = "ec951063d3b7558af8f0df31c8028a5b"

def get_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    r = requests.get(url)
    return r.json()

def get_aqi(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    r = requests.get(url)
    return r.json()

def main():
    city = input("Please enter a city to check the weather (e.g., Beijing, London):").strip()
    if ',' not in city and city.isalpha() and any(c.isupper() for c in city[1:]):\
        city = ''.join([' ' + c if c.isupper() else c for c in city]).strip()
    if not city:
        print("City name can't be empty. Exiting the program.")
        return

    forecast = get_forecast(city)
    if "list" not in forecast:
        print(f"Couldn't get the weather data for {city}. Please check if the city name is correct.")
        return

    print(f"\n📍 {city} Weather Forecast for the Next Few 3-Hour Periods: ")
    for item in forecast['list'][:8]:
        dt = datetime.datetime.fromtimestamp(item['dt'])
        temp = item['main']['temp']
        weather = item['weather'][0]['description']
        print(f"{dt}: Temperature {temp}℃，Weather {weather}")

    city_info = forecast['city']
    lat = city_info['coord']['lat']
    lon = city_info['coord']['lon']

    aqi_data = get_aqi(lat, lon)
    aqi = aqi_data['list'][0]['main']['aqi']
    print(f"\n🌫 Current Air Quality Index (AQI): {aqi} (1 = Excellent, 5 = Poor)")

    best_times = get_best_times(forecast, aqi)

    print("\n🏃 Best Times to Go Running: ")
    for b in best_times:
        print(f"{b['time']}: {b['score']} points | {b['temp']}℃ | {b['weather']} | Wind speed {b['wind']} m/s")

    plot_scores_matplotlib(best_times)
    
if __name__ == "__main__":
    main()
