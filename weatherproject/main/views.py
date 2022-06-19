import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import GraphicForm
from .models import City
from .formsWheatherCity import CityForm


# from ..data.views import cities


def index(request):
    return render(request, 'main/general.html')


def authorization(request):
    return render(request, 'main/authorization.html')


def news(request):
    return render(request, 'main/news.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def graphics(request):
    if request.method=='POST':
        form=GraphicForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = GraphicForm()
    return render(request, 'main/formGraphics.html', {'form': form})


def graphic_info(request):
    # form=GraphicForm()
    return render(request, 'main/graphic_info.html')


def weatherCity(request):
    appid = '05055e51f5b5c15967f1cfb21c3d3a55'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'pressure': res['main']['pressure'],
            'humidity': res['main']['humidity'],
            'speed': res['wind']['speed'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)

    contex = {
        'all_info': all_cities,
        'form': form
    }

    return render(request, 'main/weatherCity.html', contex)
