from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('authorization', views.authorization, name="autorization"),
    path('news', views.news, name="news"),
    path('about', views.about, name="about"),
    path('contacts',views.contacts,name="contacts")
]
