from django.urls import path
from . import views

urlpatterns = [
    path('index', views.data_index, name="data_index"),
    path('<str:city>', views.city_index, name="city_index"),
    path('<str:city>/<str:month>', views.data_home, name="data_home"),
    path('index/<str:inter>', views.data_interpolate, name="data_interpolate"),
    path('int', views.data_interpolate, name="data_index1"),
    # path('<str:user>/<str:password>', views.data_index, name="data_index")
]
