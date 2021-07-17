from django.contrib import admin
from django.db import models

from .models import Category, Vehicle, VehicleImage, VehicleSpecification, VehicleTag
# Register your models here.

class ImagesInline(admin.StackedInline):
    model = VehicleImage
    extra = 3

class SpecsInline(admin.StackedInline):
    model = VehicleSpecification
    extra = 3

class TagsInLine(admin.TabularInline):
    model = VehicleTag
    extra = 3

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ['name', 'slug']
    prepopulated_fields= {'slug': ('name', )}

@admin.register(Vehicle)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title', )}
    inlines = [ImagesInline, SpecsInline,TagsInLine]