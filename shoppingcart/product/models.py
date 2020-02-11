from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    stock = models.IntegerField()
    date_added = models.DateField(default=timezone.now)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.product_name