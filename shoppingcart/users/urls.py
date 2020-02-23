from django.urls import path
from . import views  

urlpatterns = [
    path('gender_select', views.gender_select, name='users-gender_select'),
    path('male/', views.male, name='users-male'),
    path('', views.welcome, name='users-welcome'),
]