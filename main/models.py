from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:category_items', args=[self.slug])

class Vehicle(models.Model):
    category = models.ForeignKey(Category, related_name="vehicle", on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL , related_name="vehicle_creator", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description =models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.CharField(max_length=255)
    price = models.DecimalField(max_digits = 6, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    class Meta:
        verbose_name_plural = 'Vehicles'
        ordering = ('-created',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:vehicle_detail', args=[self.slug])
    