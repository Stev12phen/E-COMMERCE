from django.shortcuts import redirect, render, HttpResponse


def cart_view(request):
    return render(request, 'cart.html')

# Create your views here.
