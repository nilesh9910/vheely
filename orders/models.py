from decimal import Decimal
import decimal
from django.conf import settings
from django.db import models

from main.models import Vehicle
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user')
    full_name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    dest_address1 = models.CharField(max_length=250)
    dest_address2 = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    dest_city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    dest_post_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now = True)
    total_paid = models.DecimalField(max_digits=8, decimal_places=2)
    order_key = models.CharField(max_length=200)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ('created', )
    
    def __str__(self):
        return str(self.created)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.id)