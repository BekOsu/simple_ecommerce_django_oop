from django.shortcuts import render
from .models import Cart
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from product.models import Product
import json
from  auth_service.services import store_cart_to_session, get_cart_from_session

     
def index(request):
    user = request.user
    cart_items = get_cart_from_session(request)
    template = loader.get_template('cart/index.html')
    context = {
        'cart_items': cart_items,
    }
    return HttpResponse(template.render(context, request))


def remove(request):
    cart = Cart.objects.get(pk=1)
    product_id = request.GET["product_id"]
    # product_id = 2
    cart.remove_cart_item(product_id)
    cart.save()
    store_cart_to_session(request,  cart.cart_items)
    return redirect('/cart/list')

def add(request):
    cart = Cart.objects.get(pk=1)
    product_id = request.GET["product_id"]
    cart.add_cart_item(int(product_id),1)
    cart.save()
    store_cart_to_session(request, cart.cart_items)
    return redirect('/cart/list')

def empty(request):
    cart = Cart.objects.get(pk=1)
    cart.empty_cart_item()
    # cart.save()
    store_cart_to_session(request,cart.cart_items)
    cart_items = cart.cart_items
    reponse = f"cart items: {cart_items}"
    return redirect('/cart/list')
 
