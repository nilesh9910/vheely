from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Category, Vehicle

def index(request):
    categories = Category.objects.all()
    return render(request, "main/index.html", {'categories': categories})

def category_items(request, slug):
    category_vehicles = get_object_or_404(Category, slug=slug).vehicle.all()
    print(category_vehicles)
    return render(request, "main/category.html", {'category_vehicles': category_vehicles})

def vehicle_detail(request, vehicle_slug):
    all_details = get_object_or_404(Vehicle, slug=vehicle_slug)
    print(all_details)
    return render(request, "main/vehicle_detail.html", {'all_details': all_details})

