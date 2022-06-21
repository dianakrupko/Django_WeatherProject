import datetime
from array import array

import requests
from django.shortcuts import render, redirect

from .forms import GraphicForm
from .formsWheatherCity import CityForm
from .graphics import *
from .models import City

import pdfkit

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version


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
    s=graphics_2('lviv', '2012-01-01 00:00', '2012-01-14 00:00')
    data={'d':s}
    # graphics_4('kyiv', '2012-01-01 00:00', '2012-01-14 00:00')
    return render(request, 'main/contacts.html',data)


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

    graphics_3(city, date1, date2)
    # graphics_2(city, date1, date2)
    # graphics_4(city, date1, date2)
    graphics_1(city, date1, date2)
    s2=graphics_2(city, date1, date2)
    s4 = graphics_4(city, date1, date2)
    # data = {'d': s}
    context = {'d2': s2,'d4': s4,'form': form, 'city': cities[city],
               'date1': date1,
               'date2': date2}
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_url("http://127.0.0.1:8000/info", "zvit.pdf", configuration=config)
    return render(request, 'main/graphic_info.html', context)


def info(request):
    date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M')
    data={'date':date}
    return render(request, 'main/info.html',data)


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

    server = 'smtp.ukr.net'
    user = 'dianakru@ukr.net'
    password = 'k3KQVjTaaKtbEUaR'

    recipients = ['dnkrupkoo@gmail.com', 'karaimivanna@gmail.com']
    sender = 'dianakru@ukr.net'
    subject = 'Звіт'
    # text = 'Текст  sdf sdf sdf sdaf <b>sdaf sdf</b> fg hsdgh <h1>f sd</h1> dfhjhgs sd gsdfg sdf'
    # html = '<html><head></head><body><p>' + text + '</p></body></html>'

    filepath = "zvit.pdf"
    basename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Diana Krupko <' + sender + '>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())

    # part_text = MIMEText(text, 'plain')
    # part_html = MIMEText(html, 'html')
    part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
    part_file.set_payload(open(filepath, "rb").read())
    part_file.add_header('Content-Description', basename)
    part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
    encoders.encode_base64(part_file)

    # msg.attach(part_text)
    # msg.attach(part_html)
    msg.attach(part_file)

    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()
    date=datetime.datetime.today().strftime('%Y-%m-%d %H:%M')
    data={'date':date}
    return render(request, 'main/report_done.html',data)
