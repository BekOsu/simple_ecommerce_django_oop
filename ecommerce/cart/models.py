from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    
    
    def add_cart_item():
        pass
    
    def remove_cart_item():
        pass
    
    def list_cart_item():
        pass
      
    def empty_cart_item():
        pass