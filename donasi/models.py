from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donasi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    amount = models.IntegerField()
    date = models.DateField(auto_now=True)
    target = models.CharField(max_length=250, null=True)