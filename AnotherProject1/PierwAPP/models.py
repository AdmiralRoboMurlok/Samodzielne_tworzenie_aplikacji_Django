from django.db import models

# Create your models here.
class Skelp(models.Model):
    klucz = models.FloatField()

class Chusteczki(models.Model):
    nazwa = models.CharField(max_length=120)
    ilosc = models.IntegerField()
    lokacja = models.ForeignKey(Skelp, on_delete=models.CASCADE)