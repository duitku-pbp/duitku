
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Investment(models.Model):
    investment_name = models.CharField(max_length = 64)
    investment_type = models.CharField(max_length = 64)
    cagr_1Y = models.DecimalField(max_digits=6, decimal_places=2)
    drawdown_1Y = models.DecimalField(max_digits=6, decimal_places=2)
    aum = models.CharField(max_length = 64)
    expense_ratio = models.DecimalField(max_digits=6, decimal_places=2)
    min_buy = models.IntegerField()
    def __str__():
        return Investment.investment_name

class Portofolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    bought_value = models.IntegerField()
