from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_home, name="data_home"),
    path('index/<str:inter>', views.data_interpolate, name="data_interpolate"),
    path('index', views.data_index, name="data_index"),
    path('int', views.data_interpolate, name="data_index1"),
    # path('<str:user>/<str:password>', views.data_index, name="data_index")
]