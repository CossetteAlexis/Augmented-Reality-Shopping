from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='product-home'),
    path('about/', views.about, name='product-about'),
    path('customer/', views.customer, name='product-customer'),
   # path('', views.button),
    path('output/', views.output,name="script"),
    path('external/', views.external),
]