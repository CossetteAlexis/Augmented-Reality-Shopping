from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    stock = models.IntegerField()
    script = models.CharField(max_length=100, default='asd')
    image = models.ImageField(default='default.jpg', upload_to='product_pic')
    date_added = models.DateField(default=timezone.now)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.product_name

class Male_Eyeglasse(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    stock = models.IntegerField()
    script = models.CharField(max_length=100, default='asd')
    image = models.ImageField(default='default.jpg', upload_to='product_pic')
    date_added = models.DateField(default=timezone.now)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.product_name

class Male_Necklace(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    stock = models.IntegerField()
    script = models.CharField(max_length=100, default='asd')
    image = models.ImageField(default='default.jpg', upload_to='product_pic')
    date_added = models.DateField(default=timezone.now)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.product_name

class Male_Cap(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    stock = models.IntegerField()
    script = models.CharField(max_length=100, default='asd')
    image = models.ImageField(default='default.jpg', upload_to='product_pic')
    date_added = models.DateField(default=timezone.now)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.product_name

class Male_Earring(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    stock = models.IntegerField()
    script = models.CharField(max_length=100, default='asd')
    image = models.ImageField(default='default.jpg', upload_to='product_pic')
    date_added = models.DateField(default=timezone.now)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.product_name

class Female_Eyeglasse(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    stock = models.IntegerField()
    script = models.CharField(max_length=100, default='asd')
    image = models.ImageField(default='default.jpg', upload_to='product_pic')
    date_added = models.DateField(default=timezone.now)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.product_name

class Female_Necklace(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    stock = models.IntegerField()
    script = models.CharField(max_length=100, default='asd')
    image = models.ImageField(default='default.jpg', upload_to='product_pic')
    date_added = models.DateField(default=timezone.now)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.product_name

class Female_Cap(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    stock = models.IntegerField()
    script = models.CharField(max_length=100, default='asd')
    image = models.ImageField(default='default.jpg', upload_to='product_pic')
    date_added = models.DateField(default=timezone.now)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.product_name

class Female_Earring(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    stock = models.IntegerField()
    script = models.CharField(max_length=100, default='asd')
    image = models.ImageField(default='default.jpg', upload_to='product_pic')
    date_added = models.DateField(default=timezone.now)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.product_name

