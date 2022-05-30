from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    summery     = models.TextField(default='Il est default value')
