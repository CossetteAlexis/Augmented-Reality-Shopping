from django.db.models.signals import post_save
from django.contrib.auth.models import Product
from django.dispatch import receiver
from .models import Cart