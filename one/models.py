from django.db import models

class Perf(models.Model):
    login = models.CharField(max_length=12)
    password = models.IntegerField()
class Product(models.Model):
    user = models.ForeignKey(Perf, on_delete=models.CASCADE)
    price = models.IntegerField()
# Create your models here.
