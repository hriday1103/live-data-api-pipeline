import requests
import pandas as pd


cities = {
    "Delhi": {"lat": 28.61, "lon": 77.20},
    "New York": {"lat": 40.71, "lon": -74.00},
    "London": {"lat": 51.50, "lon": -0.12},
    "Tokyo": {"lat": 35.67, "lon": 139.65}
}

print("--- Initializing Live Global Weather Analytics Tracker ---")
weather_data_list = []


for city_name, coords in cities.items():
    
    url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current_weather=true"
    
    response = requests.get(url)
    raw_data = response.json()

    print(raw_data)
    
    
    current = raw_data["current_weather"]
    
    
    city_report = {
        "City": city_name,
        "Temperature (°C)": current["temperature"],
        "Wind Speed (km/h)": current["windspeed"],
        "Weather Code": current["weathercode"]
    }
    
    
    weather_data_list.append(city_report)


df = pd.DataFrame(weather_data_list)


print("\n--- Live Global Climate Matrix ---")
print(df.to_string(index=False))