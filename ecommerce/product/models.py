from django.db import models
from datetime import datetime
# Create your models here.



# Create your models here.
class Product(models.Model):
    name  = models.CharField( max_length=20 )
    description = models.CharField( max_length=2000 )
    code  = models.CharField( max_length=20 )
    price  =  models.DecimalField(max_digits = 5, decimal_places = 2)
    photos  = models.CharField( max_length=20 )
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)