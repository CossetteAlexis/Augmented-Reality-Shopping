from django.urls import path
from . import views  
from django.urls import re_path
from .views import VideoCamera

urlpatterns = [
    path('video/', views.video, name='product-video'),
    path('home/', views.home, name='product-home'),
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
    path('female_caps/', views.female_caps, name='product-female_caps'),
    # path('product/female_caps/(?P<id>[0-9]+)$', views.female_caps, name='product-female_caps'),
    # re_path(r'^(?P<product_id>[0-9])/$', views.female_caps, name='product-female_caps'),
    # path('female_caps/', ProductListView.as_view(), name='product-female_caps'),
    path('female_earring/', views.female_earring, name='product-female_earrings'),
    path('face_detect/', views.VideoCamera.face_detect, name='product-face_detect'),
    path('face_detect2/', views.VideoCamera.face_detect, name='product-face_detect2'),
]