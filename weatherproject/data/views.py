from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .models import Lviv, Employee
# Add this line to the beginning of relative.py file
import sys
sys.path.append('..')

# Now you can do imports from one directory top cause it is in the sys.path
import new_data

# And even like this:
from new_data import delete_table


def data_home(request):
    return render(request, 'main/authorization.html')


def data_all(request):
    new = Lviv.objects.all()
    return render(request, 'main/index.html')


def data_index(request):
    all_employee = Employee.objects.all()
    # for e in all_employee:
        # if e.login == username and e.password == password:
        #     return render(request, 'data/index.html')
    # return render(request, 'main/authorization.html', {'error': "ERROR"})
    data = {
        "values": ["linear", "polynomial"]
    }
    return render(request, 'data/index.html', data)


def data_interpolate(request):
    print(4362536)
    # print(list2)
    r = request.GET.get("list2", "")
    print(r)
    new_data.py.delete_table("db.sqlite3")
    return render(request, "data/index.html")

