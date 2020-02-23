from django.shortcuts import render
from .models import Product
from .models import Female_Cap
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import UserForm
from . import ProductListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    PostListView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
        
"""products = [
    {
        'product_name':'Eyeglasses1',
        'brand':'Rayban',
        'price':'300',
        'date_added':'June 26, 2019'
    },
    {
        'product_name':'Eyeglasses2',
        'brand':'Tom Ford',
        'price':'500',
        'date_added':'June 27, 2019'
    }
]"""



    #from blog.models import Post
    #from django.contrib.auth.models import User
    #product = Product(product_name='adf',brand='asd',price=11,stock=123,script='asd',image_directory='ad',buyer=user)
    # return render(request, 'product/home.html')
    # context = {
    #     'products': Product.objects.all()
    # }

def male_products(request):
    return render(request, 'product/male_products.html')

def male_eyeglasses(request):
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/male_eyeglasses.html', {'page_obj': page_obj})

def male_necklace(request):
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/male_necklace.html', {'page_obj': page_obj})

def male_caps(request):
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/male_caps.html', {'page_obj': page_obj})

def male_earrings(request):
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/male_earrings.html', {'page_obj': page_obj})

def female_products(request):
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/female_products.html', {'page_obj': page_obj})

def female_eyeglasses(request):
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/female_eyeglasses.html', {'page_obj': page_obj})

def female_necklace(request):
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/female_necklace.html', {'page_obj': page_obj})

def female_caps(request):
    product = Female_Cap.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/female_caps.html', {'page_obj': page_obj})

def female_earrings(request):
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/female_earrings.html', {'page_obj': page_obj})



def about(request):
    return render(request, 'product/about.html')

def customer(request):
    return render(request, 'product/customer.html')

class ProductListView(ListView):
    model = Product
    template_name = 'product/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'products'
    ordering = ['-date_added']
