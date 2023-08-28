from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    Email=models.EmailField(max_length=254)
    phone=models.IntegerField()
    des=models.TextField(max_length=300)