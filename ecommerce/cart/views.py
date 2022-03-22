from django.shortcuts import render
from .models import Cart
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from product.models import Product
import json

def get_logged_user_cart(request):
    if request.user.is_authenticated:
         user = request.user
         cart,_ = Cart.objects.get_or_create(id=user.id)
         return cart
     
     
def get_cart_from_session(request):
    if request.user.is_authenticated:
         cart_items = json.loads(request.session['cart_items'])
         cart = get_logged_user_cart(request)
         return (cart.get_cart_products_info(cart_items))


def store_cart_to_session(request):
    if request.user.is_authenticated:
        cart = get_logged_user_cart(request)
        request.session['cart_items'] = json.dumps(cart.cart_items)
     
     
def index(request):
    user = request.user
    store_cart_to_session(request)
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
    return redirect('/cart/list')

def add(request):
    cart = Cart.objects.get(pk=1)
    product_id = request.GET["product_id"]
    cart.add_cart_item(int(product_id),1)
    cart.save()
    return redirect('/cart/list')

def empty(request):
    cart = Cart.objects.get(pk=1)
    cart.empty_cart_item()
    cart.save()
    cart_items = cart.cart_items
    reponse = f"cart items: {cart_items}"
    return redirect('/cart/list')
 
