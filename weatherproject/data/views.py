from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .models import Lviv, Employee
# Add this line to the beginning of relative.py file
import sys
sys.path.append('..')
interp="Лінійна інтерполяція"
my_dict={"linear": "Лінійна інтерполяція", "polynomial":"Поліноміальна інтерполяція", "cubic":"Кубічна інтерполяція", "spline": "Сплайн-інтерполяція"}
cities = {"lviv": "Львів", "kyiv": "Київ", "ivano_frankivsk": "Івано-франківськ", "dnipropetrovsk": "Дніпропетровськ","donetsk": "Донецьк","krivoy_rog": "Кривий ріг", "luhansk": "Луганськ", "odessa":"Одеса", "kharkiv":"Харків", "simferopol":"Сімферополь"}
months = {"01": "січень","02": "лютий","03": "березень","04": "квітень","05": "травень","06": "червень","07": "липень","08": "серпень","09": "вересень","10": "жовтень","11": "листопад","12": "грудень"}
# Now you can do imports from one directory top cause it is in the sys.path
import new_data

# And even like this:
from new_data import delete_table


def data_home(request, city, month):
    str = "2012-{:}".format(month)
    data = {
        "values": new_data.search("db.sqlite3", str, city),
        "city": cities[city],
        "month": months[month]
    }
    return render(request, 'data/my_data.html', data)


def data_all(request):
    new = Lviv.objects.all()
    return render(request, 'main/index.html')


def data_index(request):
    # all_employee = Employee.objects.all()
    # for e in all_employee:
    #     if e.login == user and e.password == password:
    data = {
        "values": ["linear", "polynomial"],
        "int": str(interp)
    }
    return render(request, 'data/index.html', data)
    # return render(request, 'main/authorization.html', {'error': "ERROR"})


def city_index(request, city):
    data = {
        "city_ua":cities[city],
        "city":city
    }
    return render(request, 'main/index.html', data)


def data_interpolate(request, inter):
    print(4362536)
    global interp
    interp = my_dict[inter]
    print(inter)
    new_data.delete_table("db.sqlite3")
    new_data.edit(inter)
    data = {
        "int": interp
    }
    return render(request, "data/index.html", data)

