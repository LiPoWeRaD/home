from django.db import models

class Perf(models.Model):
    name = models.CharField(max_length=10)
    login = models.CharField(max_length=12)
    password = models.IntegerField()
class Stat(models.Model):
    login = models.ForeignKey(Perf, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    text = models.TextField()
    date = models.DateField()
# Create your models here.
