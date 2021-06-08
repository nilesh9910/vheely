from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name="index"), 
    path('<slug:slug>/', views.category_items, name="category_items"),
    path('vehicle/<slug:vehicle_slug>/', views.vehicle_detail, name="vehicle_detail"),
]
