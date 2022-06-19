import datetime

from django import forms
from django.core.exceptions import ValidationError

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
        'placeholder': '2012-01-01 00:00',
        'min': '2012-01-01 00:00'
    }))

    date2 = forms.DateTimeField(label="До", widget=forms.DateTimeInput(attrs={
        'class': 'date',
        'placeholder': '2012-12-31 23:59',
        'max': '2012-12-12 23:59'
    }))

    def clean_date1(self):
        date1 = self.cleaned_data['date1']
        return date1.strftime("%Y-%m-%d %H:%M")

    def clean_date2(self):
        date2 = self.cleaned_data['date2']
        date1 = self.cleaned_data['date1']
        if (date2.strftime("%Y-%m-%d %H:%M") < date1):
            raise ValidationError('Друга дата має бути пізніше першої')
        return date2.strftime("%Y-%m-%d %H:%M")
