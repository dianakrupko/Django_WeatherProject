from django.shortcuts import render
from .models import Lviv


def data_home(request):
    return render(request, 'main/index.html')


def data_all(request):
    new = Lviv.objects.all()
    return render(request, 'main/index.html')
