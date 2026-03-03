from django.urls import path
from . import views  # bu sizning views.py dan oladi

urlpatterns = [
    path('', views.index_page, name='index'),  # home_page view chaqiriladi
]