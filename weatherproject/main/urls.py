from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('authorization', views.authorization, name="autorization"),
    path('news', views.news, name="news"),
    path('about', views.about, name="about"),
    path('contacts', views.contacts, name="contacts"),
    path('weatherCity', views.weatherCity, name="weatherCity"),
    path('graphics', views.graphics, name="graphics"),
    # path('<str:date2>', views.graphic_info, name="graphic_info")
    path('graphic_info', views.graphic_info, name="graphic_info"),
    path('info', views.info, name="info"),
    path('report', views.report, name="report")

]
