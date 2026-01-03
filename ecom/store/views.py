from django.shortcuts import redirect, render, HttpResponse
from.models import Product, Category, Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from.forms import SignUpForm




# Create your views here

def admin_view(request):
    products= Product.objects.count()
    categorys= Category.objects.count()
    customers= Customer.objects.count()

    return render(request, 'admin_view.html')




def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome 🎉")
            return redirect('home')   # STOP execution here
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


def home(request):
    products= Product.objects.all()
    return  render(request, 'home.html', {'products': products})


def about(request):
    return render(request, 'about.html')
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def product(request, pk):
    product= Product.objects.get(id= pk)
    return  render(request, 'product.html', {'product': product})


def category_view(request, foo):
    foo = foo.replace('-', ' ')  # convert URL slug to name

    try:
        category = Category.objects.get(name__iexact=foo)
        products = Product.objects.filter(category=category)

        return render(request, 'category.html', {
            'category': category,
            'products': products
        })

    except Category.DoesNotExist:
        messages.error(request, 'Category does not exist')
        return redirect('home')





def logout_view(request):
    logout(request)
    return redirect('home')