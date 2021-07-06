from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name='basket'

urlpatterns = [
    path('<slug:slug>/', views.order_summary, name='basket_summary'),
    path('<slug:slug>/booked', views.confirmation, name='confirmation')
]
