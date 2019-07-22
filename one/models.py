from django.db import models

class Perf(models.Model):
    id = models.AutoField(primary_key=True)
    Имя = models.CharField(max_length=10, db_column='name')
    Логин = models.CharField(max_length=12, unique=True, db_column='login')
    Пароль = models.IntegerField(db_column='password')
class Stat(models.Model):
    Логин = models.ForeignKey(Perf, on_delete=models.CASCADE)
    Название = models.CharField(max_length=25, db_column='name')
    Информация = models.TextField(db_column='info')
    Дата = models.DateField(db_column='Date')
# Create your models here.

