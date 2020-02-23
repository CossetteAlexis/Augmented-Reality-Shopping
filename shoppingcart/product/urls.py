from django.urls import path
from . import views  
from . import ProductListView

urlpatterns = [
    path('about/', views.about, name='product-about'),
    path('customer/', views.customer, name='product-customer'),
    path('male_products/', views.male_products, name='product-male_products'),
    path('male_eyeglasses/', views.male_eyeglasses, name='product-male_eyeglasses'),
    path('male_necklace/', views.male_necklace, name='product-male_necklace'),
    path('male_caps/', views.male_caps, name='product-male_caps'),
    path('male_earrings/', views.male_earrings, name='product-male_earrings'),
    path('female_products/', views.female_products, name='product-female_products'),
    path('female_eyeglasses/', views.female_eyeglasses, name='product-female_eyeglasses'),
    path('female_necklace/', views.female_necklace, name='product-female_necklace'),
    path('female_caps/', PostListView().as_view(), name='product-female_caps'),
    path('female_earrings/', views.female_earrings, name='product-female_earrings'),
]