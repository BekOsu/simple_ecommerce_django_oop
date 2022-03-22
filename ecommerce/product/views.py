from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from product.models import Product
import json
from cart.models import Cart
# Create your views here.
def index(request):
    products = Product.objects.all()
    template = loader.get_template('product/index.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))