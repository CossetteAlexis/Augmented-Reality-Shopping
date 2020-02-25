from django.urls import path
from . import views  
from django.urls import re_path
from .views import VideoCamera
from .views import Female_CapListView
from .views import Female_CapDetailView
from .views import Female_EyeglassesListView
from .views import Female_EyeglassesDetailView
from .views import Female_EarringListView
from .views import Female_EarringDetailView
from .views import Female_NecklaceListView
from .views import Female_NecklaceDetailView
from .views import Male_EarringListView
from .views import Male_Earring
from .views import Male_CapsListView
from .views import Male_CapsDetailView
from .views import Male_NecklaceListView
from .views import Male_NecklaceDetailView
from .views import Male_EarringListView
from .views import Male_EyeglassesgDetailView

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
    path('female_earring/', views.female_earring, name='product-female_earrings'),
    path('face_detect/<int:pk>/', views.VideoCamera.face_detect, name='product-face_detect'),
    path('face_detect2/', views.VideoCamera.face_detect, name='product-face_detect2'),
    path('face_detect3/<int:pk>/', views.VideoCamera.face_detect3, name='product-face_detect3'),
    path('face_detect4/<int:pk>/', views.VideoCamera.face_detect4, name='product-face_detect4'),
    # path('female_caps/', views.female_caps, name='product-female_caps'),
    path('female_caps/', Female_CapListView.as_view(), name='product-female_caps'),
    path('female_caps/<int:pk>/', Female_CapDetailView.as_view(), name='product-female_caps_detail'),
    path('female_eyeglasses/', Female_EyeglassesListView.as_view(), name='product-female_eyeglasses'),
    path('female_eyeglasses/<int:pk>', Female_EyeglassesDetailView.as_view(), name='product-female_eyeglasses_detail'),
    path('product/<int:pk>/', Female_EyeglassesDetailView.as_view(), name='product-female_eyeglasses_detail'),
]