from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .cart import Cart
from store.models import Product




def cart_summary(request):
    return render(request, 'cart_summary.html')

# Create your views here.
def cart_add(request):
   #get the cart
   cart= Cart(request)
   #test for post
   if request.POST.get('action')== 'post':
       #get the staff
       product_id= int(request.POST.get('product_id'))
       #lookup the product in db
       product= get_object_or_404(Product, id= product_id)
       #save to session
       cart.add(product= product)
       #retuen a response

       cart_quantity= cart.__len__()
       response= JsonResponse({'cart_quantity': cart_quantity})

       response= JsonResponse({'Product Name:':product.name})
       return response 









def cart_delete(request):
    pass
def cart_update(request):
    pass
