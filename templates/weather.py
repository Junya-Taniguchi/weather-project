import requests
import json

city = "London"
APIkey = "6006c8a1d90dd8e603fc35057667698f"

api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID="+APIkey
r = requests.get(api)
data = json.loads(r.text)

k2c = lambda k: k - 273.15

print("+ 都市=", data["name"])
print("| 天気=", data["weather"][0]["description"])
print("| 最低気温=", k2c(data["main"]["temp_min"]))
print("| 最高気温=", k2c(data["main"]["temp_max"]))
print("| 湿度=", data["main"]["humidity"])
print("| 気圧=", data["main"]["pressure"])
# print("| 風向き=", data["wind"]["deg"]) 読み込めない‥
print("| 風速度=", data["wind"]["speed"])
print("| 国名=",data["sys"]["country"])
print("")
