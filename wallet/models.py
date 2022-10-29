from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Wallet(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    balance = models.FloatField(default=0)


class TransactionType(models.TextChoices):
    INCOME = 'INCOME'
    OUTCOME = 'OUTCOME'


class Transaction(models.Model):
    wallet = models.ForeignKey(to=Wallet, on_delete=models.CASCADE)
    amount = models.FloatField()
    done_on = models.DateField(default=timezone.now)
    type = models.CharField(
        max_length=len(TransactionType.OUTCOME), choices=TransactionType.choices
    )
    description = models.TextField(null=True)
