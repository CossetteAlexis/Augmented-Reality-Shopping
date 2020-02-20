from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
import sys
from subprocess import run,PIPE

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


def home(request):
    #from blog.models import Post
    #from django.contrib.auth.models import User
    #product = Product(product_name='adf',brand='asd',price=11,stock=123,script='asd',image_directory='ad',buyer=user)
    # return render(request, 'product/home.html')
    # context = {
    #     'products': Product.objects.all()
    # }
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/home.html', {'page_obj': page_obj})
    #return render(request, 'product/home.html', )

def about(request):
    return render(request, 'product/about.html')

def customer(request):
    return render(request, 'product/customer.html')

# def button(request):
#     return render(request,'prhome.html')

