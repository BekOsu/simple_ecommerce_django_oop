from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from product.models import Product
import json
from cart.models import Cart
from django.contrib.sessions.backends.db import SessionStore
# Create your views here.

s = SessionStore()
def index(request):

    products = Product.objects.all()
    template = loader.get_template('product/index.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))


def login(request):
    # m = User.objects.get(username=request.POST['username'])
    # if m.check_password(request.POST['password']):
    #     request.session['member_id'] = m.id
    #     return HttpResponse("You're logged in.")
    # else:
        return HttpResponse("Your username and password didn't match.")