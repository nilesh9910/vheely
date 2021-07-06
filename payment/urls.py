from django.urls import path

from . import views

app_name='payment'

url_patterns = [
    path('', views.BasketView, name='basket'),
]