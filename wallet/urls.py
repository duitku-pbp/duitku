from django.urls import path

from wallet.views import (
    create_transaction,
    create_transaction_page,
    create_wallet,
    create_wallet_page,
    fetch_transactions,
    fetch_wallets,
    index,
    report_for_month,
    transaction_detail,
    transaction_detail_page,
    transactions_page,
    wallet_detail,
    wallet_detail_page,
)


app_name = 'wallet'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', wallet_detail_page, name='wallet-detail'),
    path('api/report/<str:period>/', report_for_month, name='report-for-month'),
    path('create/', create_wallet_page, name='create-wallet'),
    path('api/create/', create_wallet, name='api-create-wallet'),
    path('api/', fetch_wallets, name='api-fetch-wallets'),
    path('api/<int:id>/', wallet_detail, name='api-wallet-detail'),
    path('transaction/', transactions_page, name='transactions'),
    path('api/transaction/', fetch_transactions, name='api-fetch-transactions'),
    path('transaction/create/', create_transaction_page, name='create-transaction'),
    path('api/transaction/create/', create_transaction, name='api-create-transaction'),
    path('transaction/<int:id>/', transaction_detail_page, name='transaction-detail'),
    path(
        'api/transaction/<int:id>/', transaction_detail, name='api-transaction-detail'
    ),
]
