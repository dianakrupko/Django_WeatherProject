from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .models import Lviv, Employee
from ..new_data import delete_table


def data_home(request):
    return render(request, 'main/authorization.html')


def data_all(request):
    new = Lviv.objects.all()
    return render(request, 'main/index.html')


def data_index(request, username, password):
    all_employee = Employee.objects.all()
    for e in all_employee:
        if e.login == username and e.password == password:
            return render(request, 'data/index.html')
    return render(request, 'main/authorization.html', {'error': "ERROR"})


def data_interpolate(request, inter):
    delete_table("db.sqlite3")
    return render(request, "data/index.html")

