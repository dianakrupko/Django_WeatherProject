from django import forms

from .models import *


class GraphicForm(forms.Form):
    cities = {"lviv": "Львів", "kyiv": "Київ", "ivano_frankivsk": "Івано-франківськ",
              "dnipropetrovsk": "Дніпропетровськ", "donetsk": "Донецьк", "krivoy_rog": "Кривий ріг",
              "luhansk": "Луганськ", "odessa": "Одеса", "kharkiv": "Харків", "simferopol": "Сімферополь"}
    CITY_CHOICES = (
        # ("", "Виберіть регіон"),
        ("lviv", "Львів"),
        ("kyiv", "Київ"),
        ("donetsk", "Донецьк"),
        ("krivoy_rog", "Кривий Ріг"),
        ("odessa", "Одеса"),
    )
    city = forms.ChoiceField(choices=CITY_CHOICES, label="Регіон")
    date1 = forms.DateTimeField(label='З', input_formats=['%d/%m/%Y %H:%M'], widget=forms.DateTimeInput(attrs={
        'class': 'date',
        'placeholder':'2012-01-01 00:00:00',
        'min':'2012-01-01 00:00:00'
    }))
    date2 = forms.DateTimeField(label="До",widget=forms.DateTimeInput(attrs={
        'class': 'date',
        'placeholder':'2012-12-31 23:59:59',
        'max': '2012-12-12 23:59:59'
    }))
