from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

def home(request):
    return render(request, 'home.html')

def ask(request):
    fulltext = request.GET['fulltext']
    city = fulltext
    APIkey = "6006c8a1d90dd8e603fc35057667698f"

    api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID="+APIkey
    r = requests.get(api)
    data = json.loads(r.text)

    k2c = lambda k: k - 273.15
    name = data["name"]
    weather = data["weather"][0]["description"]
    ondo = k2c(data["main"]["temp_min"])
    return render(request, 'ask.html' ,{'name' : name,'weather': weather,'ondo': ondo})
