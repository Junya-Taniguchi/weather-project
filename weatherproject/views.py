from django.http import HttpResponse
from django.shortcuts import render
import requests
import json


def home(request):
    return render(request, 'home.html')


def ask(request):
    city = request.GET['city']
    city = city
    APIkey = "your APIkey"

    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" + APIkey
    r = requests.get(api)
    data = json.loads(r.text)

    def k2c(k): return k - 273.15
    name = data["name"]
    weather = data["weather"][0]["description"]
    temp_max = k2c(data["main"]["temp_max"])
    temp_min = k2c(data["main"]["temp_min"])
    return render(request, 'ask.html', {'name': name, 'weather': weather, 'temp_max': temp_max, 'temp_min': temp_min})
