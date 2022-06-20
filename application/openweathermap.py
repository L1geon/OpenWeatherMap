import requests


def get_weather(city: str):
    api = ""
    params = {"q": city, "type": "like", "units": "metric", "lang": "ru", "APPID": api}
    r = requests.get("http://api.openweathermap.org/data/2.5/find", params=params)
    data = r.json()
    print(f"""        id города в системе OpenWeatherMap: {data["list"][0]["id"]}
        Координаты города: {data["list"][0]["coord"]}
        Текущая температура: {data["list"][0]["main"]["temp"]}°C
        Облака: {data["list"][0]["weather"][0]["description"]}""")


if __name__ == "__main__":
    get_weather()
