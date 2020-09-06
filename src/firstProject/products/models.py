from django.db import models


# Create your models here.
class Product(models.Model): # Inheriting from model.Model
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
