from django.urls import path
from . import views
from django.views.generic.base import TemplateView

app_name = "main"

urlpatterns = [
    path('', views.index, name="index"), 
    path('about-us/', TemplateView.as_view(template_name='main/about_us.html'), name='about_us'),
    path('contact-us/', TemplateView.as_view(template_name='main/contact_us.html'), name='contact_us'),
    path('<slug:slug>/', views.category_items, name="category_items"),
    path('vehicle/<slug:vehicle_slug>/', views.vehicle_detail, name="vehicle_detail"),
]
