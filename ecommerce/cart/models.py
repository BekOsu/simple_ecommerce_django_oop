from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import json
from django.core import serializers
import json
from jsonfield import JSONField

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
    
    
    # def set_cart_item(self, data):
    #       cart_items =   json.dumps(data)
        
    # def get_cart_item(self):
    #         return json.loads(self.cart_items)
        
    def add_cart_item(self, product_id, quantity): 

        new_item =  {'product_id':product_id,
                     'quantity': quantity}
        
        self.cart_items.append(json.dumps(new_item))

    
    def remove_cart_item(self, product_id):
        index = 0
        for item in self.cart_items:
          item = json.loads(item)
          if item['product_id']  == product_id:
              self.cart_items.pop(index)
          index += 1
    
      
    def empty_cart_item(self):
     self.cart_items.clear()
     return self
 
 
 # todo
 # add users seasions 
 # increes/ decares product quantity 
 # add views
 # add photots