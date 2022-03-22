from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import json
from django.core import serializers
import json
from jsonfield import JSONField
from product.models import Product
from django.contrib.sessions.backends.db import SessionStore

class CartItem():
    
    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity
 
    def tojson(self, data):
          cart_items =   json.dumps(data)
        


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    cart_items = JSONField(null=True, blank=True)
    
    def add_cart_item(self, product_id, quantity): 
        index = 0
        for item in self.cart_items:
          item = json.loads(item)
          if item['product_id']  == int(product_id):
              quantity = int(item['quantity'] )
              item['quantity'] = quantity + 1
              self.cart_items[index] = json.dumps(item)
              return 
          index += 1
          
        new_item =  {'product_id':product_id,
                     'quantity': quantity}
        
        self.cart_items.append(json.dumps(new_item))

    
    def remove_cart_item(self, product_id):
        index = 0
        for item in self.cart_items:
          item = json.loads(item)
          if item['product_id']  == int(product_id):
              quantity = int(item['quantity'] )
              quantity -= 1
              
              item['quantity'] = quantity
              if quantity < 1:
                self.cart_items.pop(index)
              else: 
                 self.cart_items[index] = json.dumps(item)
              
              return 
          index += 1
    
      
    def empty_cart_item(self):
     self.cart_items.clear()
     return self
 
 
    def get_cart_products_info(self, cart_items = None ):
            if cart_items is None:
                cart_items = self.cart_items
            index = 0
            for item in cart_items:
                _item = json.loads(item)
                product = Product.objects.get(pk = _item['product_id'])
                product_info = dict(id=product.id,
                                    name=product.name,
                                    price=product.price,
                                    description=product.description,
                                    photo=product.photos,
                                    code=product.code,
                                    quantity=_item['quantity'])
                cart_items[index] = product_info
                index += 1
            return cart_items
        
        
 # todo
 # add photots