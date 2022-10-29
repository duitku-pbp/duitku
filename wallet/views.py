import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from wallet.helpers import write_json_response
from wallet.models import Transaction, Wallet

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

        Wallet.objects.create(
            owner=req.user,
            name=data["name"],
            description=data["description"],
            balance=data["initial-balance"],
        )

        return redirect("wallet:index")

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
