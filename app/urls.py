from django.urls import path
from . import views  # bu sizning views.py dan oladi

urlpatterns = [
    path('', views.home_page, name='home'),  # home_page view chaqiriladi
]