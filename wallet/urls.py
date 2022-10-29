from django.urls import path

from wallet.views import (
    create_transaction,
    create_transaction_page,
    create_wallet,
    create_wallet_page,
    fetch_transactions,
    fetch_wallets,
    index,
)


app_name = 'wallet'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_wallet_page, name='create-wallet'),
    path('api/create/', create_wallet, name='api-create-wallet'),
    path('api/', fetch_wallets, name='api-fetch-wallets'),
    path('api/transaction/', fetch_transactions, name='api-fetch-transactions'),
    path('transaction/create/', create_transaction_page, name='create-transaction'),
    path('api/transaction/create/', create_transaction, name='api-create-transaction'),
]
