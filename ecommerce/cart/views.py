from django.shortcuts import render
from .models import Cart
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from product.models import Product
import json


def index(request):
    cart = Cart.objects.get(pk=1)
    cart_items = cart.get_cart_products_info()
    template = loader.get_template('cart/index.html')
    context = {
        'cart_items': cart_items,
    }
    return HttpResponse(template.render(context, request))


def remove(request):
    cart = Cart.objects.get(pk=1)
    cart.remove_cart_item(1)
    cart.save()
    cart_items = cart.cart_items
    reponse = f"cart items: {cart_items}"
    return HttpResponse(reponse)

def add(request):
    cart = Cart.objects.get(pk=1)
    cart.add_cart_item(2,2)
    cart.save()
    cart_items = cart.cart_items
    reponse = f"cart items: {cart_items}"
    return HttpResponse(reponse)

def empty(request):
    cart = Cart.objects.get(pk=1)
    cart.empty_cart_item()
    cart.save()
    cart_items = cart.cart_items
    reponse = f"cart items: {cart_items}"
    return redirect('/cart/list')
 
