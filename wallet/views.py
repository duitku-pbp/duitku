import json
import itertools
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from wallet.helpers import write_json_response
from wallet.models import Transaction, TransactionType, Wallet

# Create your views here.
@login_required(login_url='/authentication/login')
def index(req: HttpRequest) -> HttpResponse:
    if req.method == "GET":
        return render(req, 'wallet/index.html')

    return write_json_response(405, 'Method not allowed')


@login_required(login_url='/authentication/login')
def fetch_wallets(req: HttpRequest) -> HttpResponse:
    if req.method == "GET":
        wallets = Wallet.objects.filter(owner=req.user).values()

        return write_json_response(200, list(wallets))

    return write_json_response(405, 'Method not allowed')


@login_required(login_url='/authentication/login')
def wallet_detail_page(req: HttpRequest, id: int) -> HttpResponse:
    if req.method == "GET":
        wallet: Wallet | None = Wallet.objects.filter(owner=req.user, pk=id).first()
        if wallet is None:
            return write_json_response(404, 'Wallet not found')

        return render(req, "wallet/wallet-detail.html", {'wallet': wallet})

    return write_json_response(405, 'Method not allowed')


@login_required(login_url='/authentication/login')
def fetch_transactions(req: HttpRequest) -> HttpResponse:
    if req.method == "GET":
        transactions = list(
            Transaction.objects.filter(actor=req.user)
            .order_by('-done_on', '-id')
            .values()
        )

        key_fn = lambda trx: trx['done_on']
        transactions_map_by_date = itertools.groupby(transactions, key_fn)

        transactions = []
        for date, trxs in transactions_map_by_date:
            trxs = list(trxs)
            for i in range(len(trxs)):
                trxs[i]['done_on'] = str(trxs[i]['done_on'])

            transactions.append({'date': str(date), 'transactions': trxs})

        return write_json_response(200, transactions)

    return write_json_response(405, 'Method not allowed')


@login_required(login_url='/authentication/login')
def create_wallet_page(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, 'wallet/create-wallet.html')

    return write_json_response(405, 'Method not allowed')


@login_required(login_url='/authentication/login')
def create_transaction_page(req: HttpRequest) -> HttpResponse:
    if req.method == "GET":
        return render(req, 'wallet/create-transaction.html')

    return write_json_response(405, 'Method not allowed')


@login_required(login_url='/authentication/login')
def create_wallet(req: HttpRequest) -> HttpResponse:
    if req.method == "POST":
        data = json.loads(req.body)

        wallet = Wallet(
            owner=req.user,
            name=data["name"],
            description=data["description"],
            balance=data["initial-balance"],
        )

        wallet.save()

        initial_balance = float(data["initial-balance"])
        if initial_balance != 0:
            balance, t_type = (
                (initial_balance, TransactionType.INCOME)
                if initial_balance > 0
                else (abs(initial_balance), TransactionType.OUTCOME)
            )
            transaction = Transaction(
                wallet=wallet,
                actor=req.user,
                amount=balance,
                type=t_type,
                description="Initial Balance",
            )

            transaction.save()

        return redirect("wallet:index")

    return write_json_response(405, 'Method not allowed')


@login_required(login_url='/authentication/login')
def wallet_detail(req: HttpRequest, id: int) -> HttpResponse:
    if req.method == "GET":
        wallet: Wallet | None = Wallet.objects.filter(owner=req.user, pk=id).first()
        if wallet is None:
            return write_json_response(404, 'Wallet not found')

        return write_json_response(200, model_to_dict(wallet))
    elif req.method == "PUT":
        wallet: Wallet | None = Wallet.objects.filter(owner=req.user, pk=id).first()
        if wallet is None:
            return write_json_response(404, 'Wallet not found')

        data = json.loads(req.body)

        input_balance = float(data["balance"])

        if wallet.balance != input_balance:
            amount, t_type = (
                (input_balance - wallet.balance, TransactionType.INCOME)
                if input_balance > wallet.balance
                else (wallet.balance - input_balance, TransactionType.OUTCOME)
            )

            transaction = Transaction(
                amount=amount,
                actor=req.user,
                wallet=wallet,
                type=t_type,
                description="Adjust Balance",
            )

            transaction.save()

        wallet.balance = input_balance
        wallet.name = data["name"]
        wallet.description = data["description"]

        wallet.save()

        return redirect('wallet:wallet-detail', id=id)

    elif req.method == "DELETE":
        wallet: Wallet | None = Wallet.objects.filter(owner=req.user, pk=id).first()
        if wallet is None:
            return write_json_response(404, 'Wallet not found')

        wallet.delete()

        return redirect('wallet:index')

    return write_json_response(405, 'Method not allowed')


@login_required(login_url='/authentication/login')
def transactions_page(req: HttpRequest) -> HttpResponse:
    if req.method == "GET":
        return render(req, 'wallet/transactions.html')

    return write_json_response(405, 'Method not allowed')


@login_required(login_url='/authentication/login')
def create_transaction(req: HttpRequest) -> HttpResponse:
    if req.method == "POST":
        data = json.loads(req.body)

        wallet: Wallet | None = Wallet.objects.filter(
            owner=req.user, pk=data["wallet"]
        ).first()
        if wallet is None:
            return write_json_response(404, 'Wallet does not exist')

        Transaction.objects.create(
            wallet=wallet,
            amount=data["amount"],
            type=data["type"],
            done_on=data["done-on"],
            description=data["description"],
            actor=req.user,
        )

        if data["type"] != "INCOME" and data["type"] != "OUTCOME":
            return write_json_response(400, "Invalid transaction type")
        elif data["type"] == "INCOME":
            wallet.balance += float(data["amount"])
        else:
            wallet.balance -= float(data["amount"])

        wallet.save()

        return redirect("wallet:index")

    return write_json_response(405, 'Method not allowed')
