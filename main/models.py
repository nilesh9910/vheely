from django.db import models
from django.conf import settings
from django.db.models.fields import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import math

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
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = 'Vehicles'
        ordering = ('-created',)
    
    def __str__(self):
        return self.title
    
    def first_half_spec(self):
        count = math.ceil(self.vehicle_specs.all().count()/2)
        return self.vehicle_specs.all()[:count]
    def second_half_spec(self):
        count = math.ceil(self.vehicle_specs.all().count()/2)
        return self.vehicle_specs.all()[count:]



    def get_absolute_url(self):
        return reverse('main:vehicle_detail', args=[self.slug])

class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle_image')
    image = models.ImageField(
        verbose_name=_('image'),
        help_text = 'upload an image',
        upload_to = 'images/',

    )

class VehicleSpecification(models.Model):
    """
    The Product Specification Value table holds each of the
    products individual specification or bespoke features.
    """

    product = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle_specs')
    value = models.CharField(
        verbose_name=_("value"),
        help_text=_("Vehicle specification value (maximum of 255 words)"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")

    def __str__(self):
        return self.value

class VehicleTag(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle_tags')
    tag = models.CharField(
        verbose_name=_("tag"),
        help_text=_("Enter Vehicle tags(maximum of 100 words)"),
        max_length=100,
    )
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    def __str__(self):
        return self.tag