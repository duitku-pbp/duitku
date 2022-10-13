from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  balance = models.IntegerField()