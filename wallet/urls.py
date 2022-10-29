from django.urls import path

from wallet.views import index


app_name = 'wallet'

urlpatterns = [path('', index, name='index')]
