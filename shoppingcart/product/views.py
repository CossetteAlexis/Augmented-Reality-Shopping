from django.shortcuts import render
from .models import Products

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
    #return render(request, 'product/home.html')
    context = {
        'products': Products.objects.all()
    }
    return render(request, 'product/home.html', context)

def about(request):
    return render(request, 'product/about.html')

def customer(request):
    return render(request, 'product/customer.html')