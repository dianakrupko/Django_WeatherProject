from django import forms

from .models import *


class GraphicForm(forms.Form):
    name = forms.CharField(max_length=30, label="Регіон")
    calendar = forms.DateInput()
