import requests
from django.shortcuts import render, redirect

from .forms import GraphicForm
from .formsWheatherCity import CityForm
from .graphics import *
from .models import City

import pdfkit

# import aspose.words as aw
#
# doc = aw.Document("Input.html")
# doc.save("Output.pdf")
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

    context = {'form': form, 'city': city,
               'date1': date1, 'submitbutton': submitbutton,
               'date2': date2}
    return render(request, 'main/formGraphics.html', context)


def graphic_info(request):
    city = ''
    date1 = ''
    date2 = ''
    cities = {"lviv": "Львів", "kyiv": "Київ", "ivano_frankivsk": "Івано-Франківськ",
              "dnipropetrovsk": "Кропивницький", "donetsk": "Донецьк", "krivoy_rog": "Кривий Ріг",
              "luhansk": "Луганськ", "odessa": "Одеса", "kharkiv": "Харків", "simferopol": "Сімферополь"}
    form = GraphicForm(request.POST or None)
    if form.is_valid():
        city = form.cleaned_data.get("city")
        date1 = form.cleaned_data.get("date1")
        date2 = form.cleaned_data.get("date2")
        # print(form.cleaned_data)

    context = {'form': form, 'city': cities[city],
               'date1': date1,
               'date2': date2}
    graphics_3(city, date1, date2)
    graphics_2(city, date1, date2)
    graphics_4(city, date1, date2)
    graphics_1(city, date1, date2)
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_url("http://127.0.0.1:8000/info", "zvit.pdf", configuration=config)
    return render(request, 'main/graphic_info.html', context)


def info(request):
    return render(request, 'main/info.html')


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


def report(request):

    # path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    # config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    # pdfkit.from_url("http://127.0.0.1:8000/info", "zvit.pdf", configuration=config)
    # mail.sendmail(sender, recipients, msg.as_string())
    return render(request, 'main/report_done.html')
