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
    date1 = forms.DateTimeField(label='З')
    date2 = forms.DateTimeField(label="До")
