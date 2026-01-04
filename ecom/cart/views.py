from django.shortcuts import redirect, render, HttpResponse


def cart_summary(request):
    return render(request, 'cart_summary.html')

# Create your views here.
def cart_add(request):
    return HttpResponse('hello worlds')
def cart_delete(request):
    pass
def cart_update(request):
    pass
