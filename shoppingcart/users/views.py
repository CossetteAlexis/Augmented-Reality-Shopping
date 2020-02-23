from django.shortcuts import render, redirect
from django.contrib.auth.forms  import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST )
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome  {username}!')
            return redirect('login')
    else:
            form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})


def gender_select(request):
    return render(request, 'users/gender_select.html')

def male(request):
    return redirect('users-male')

@login_required
def cart(request):
    return render(request, 'users/cart.html')

def welcome(request):
    return render(request, 'users/welcome.html')