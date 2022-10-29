from django.urls import path

from wallet.views import create_wallet, create_wallet_page, index


app_name = 'wallet'

urlpatterns = [
    path('', index, name='index'),
    path('create', create_wallet_page, name='create'),
    path('api/create', create_wallet, name='api-create'),
]
