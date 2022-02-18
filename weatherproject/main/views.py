import requests
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def authorization(request):
    return render(request, 'main/authorization.html')


def news(request):
    return render(request, 'main/news.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def weatherCity(request):
    appid = '05055e51f5b5c15967f1cfb21c3d3a55'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = "London"

    res = requests.get(url.format(city)).json()


    city_info={
        'city': city,
        'temp':res['main']['temp'],
        # 'icon':res['weather'][0]['icon']
    }
    contex={
        'info':city_info
    }

    return render(request, 'main/weatherCity.html', contex)
