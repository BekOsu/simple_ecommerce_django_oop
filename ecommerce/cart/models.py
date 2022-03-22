from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)