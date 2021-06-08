from django.contrib import admin

from .models import Category, Vehicle
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display: ['name', 'slug']
    prepopulated_fields: {'slug': ('name', )}

@admin.register(Vehicle)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title', )}