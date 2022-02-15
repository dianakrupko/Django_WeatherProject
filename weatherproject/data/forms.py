from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Employee
from django.forms import ModelForm
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = "data/index.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("employee")


