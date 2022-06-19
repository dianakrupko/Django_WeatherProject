import requests
from django.shortcuts import render, redirect

from .forms import GraphicForm
from .formsWheatherCity import CityForm
from .graphics import *
from .models import City


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
    # if request.method=='POST':
    #     form=GraphicForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    # else:
    #     form = GraphicForm()
    submitbutton = request.POST.get("submit")

    city = ''
    date1 = ''
    date2 = ''
    print(date2)
    form = GraphicForm(request.POST or None)
    if form.is_valid():
        city = form.cleaned_data.get("city")
        date1 = form.cleaned_data.get("date1")
        date2 = form.cleaned_data.get("date2")
        # print(form.cleaned_data)
    # formatDate1 = date1.strftime("%Y-%m-%d %H:%M:%S")
    # formatDate2 = date2.strftime("%Y-%m-%d %H:%M:%S")

    context = {'form': form, 'city': city,
               'date1': date1, 'submitbutton': submitbutton,
               'date2': date2}
    # print(city)
    # print(date1)
    # print(date2)
    # graphics_4('lviv', '2012-01-01 00:00', '2012-12-01 00:00')
    # graphics_4(city,date1,date2)
    return render(request, 'main/formGraphics.html', context)


def graphic_info(request):
    # form=GraphicForm()
    # if request.method == 'POST':
    #     form = GraphicForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    # else:
    #     form = GraphicForm()

    city = ''
    date1 = ''
    date2 = ''
    print(date2)
    form = GraphicForm(request.POST or None)
    if form.is_valid():
        city = form.cleaned_data.get("city")
        date1 = form.cleaned_data.get("date1")
        date2 = form.cleaned_data.get("date2")
        # print(form.cleaned_data)

    context = {'form': form, 'city': city,
               'date1': date1,
               'date2': date2}

    print(city)
    print(date1)
    print(date2)
    graphics_3(city, date1, date2)
    graphics_2(city, date1, date2)
    graphics_4(city, date1, date2)
    graphics_1(city, date1, date2)
    return render(request, 'main/graphic_info.html', context)


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
