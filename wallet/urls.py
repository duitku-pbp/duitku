from django.urls import path

from wallet.views import create_wallet, index


app_name = 'wallet'

urlpatterns = [
    path('', index, name='index'),
    path('create', create_wallet, name='create'),
]
