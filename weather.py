import requests
import json

LAT = 59.4370
LON = 24.7536

headers = {
    "User-Agent": "TallinnWeatherApp/1.0 svyat@student.edu"
}

url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={LAT}&lon={LON}"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    timeseries = data["properties"]["timeseries"]
    
    for i in range(5):
        time = timeseries[i]["time"]
        temp = timeseries[i]["data"]["instant"]["details"]["air_temperature"]
        print(f"{time} {temp}C")
else:
    print("Ошибка при запросе:", response.status_code)
