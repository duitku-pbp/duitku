from django.urls import path

from wallet.views import test


app_name = 'wallet'

urlpatterns = [path('', test, name='test')]
