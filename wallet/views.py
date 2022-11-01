import calendar
import json
import itertools

from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render

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
def report_for_month(req: HttpRequest, period: str) -> HttpResponse:
    if req.method == "GET":
        start_date, end_date = "", ""

        try:
            start_date = datetime.strptime(period, "%Y-%m").date()
            end_date = start_date.replace(
                day=calendar.monthrange(start_date.year, start_date.month)[1]
            )
        except ValueError:
            return write_json_response(400, 'Invalid period')

        cur_month_income = Transaction.objects.filter(
            actor=req.user,
            type=TransactionType.INCOME,
            done_on__gte=start_date,
            done_on__lte=end_date,
        ).aggregate(income=Sum('amount'))

        cur_month_outcome = Transaction.objects.filter(
            actor=req.user,
            type=TransactionType.OUTCOME,
            done_on__gte=start_date,
            done_on__lte=end_date,
        ).aggregate(outcome=Sum('amount'))

        report = dict()
        report.update(cur_month_income)
        report.update(cur_month_outcome)

        if report["income"] is None:
            report["income"] = 0
        if report["outcome"] is None:
            report["outcome"] = 0

        report['net_income'] = report['income'] - report['outcome']
        report['period'] = start_date.strftime("%m/%Y")

        return write_json_response(200, report)

    return write_json_response(405, 'Method not allowed')


@login_required(login_url='/authentication/login')
def fetch_transactions(req: HttpRequest) -> HttpResponse:
    if req.method == "GET":
        wallet_id = req.GET.get('from-wallet', 'all')

        transactions = []

        def map_transaction(trx: Transaction):
            trx_obj = model_to_dict(trx)
            trx_obj['wallet'] = model_to_dict(trx.wallet)
            trx_obj['done_on'] = str(trx.done_on)

            return trx_obj

        if wallet_id == 'all':
            transactions = list(
                map(
                    map_transaction,
                    list(
                        Transaction.objects.select_related('wallet')
                        .filter(actor=req.user)
                        .order_by('-done_on', '-id')
                    ),
                )
            )
        else:
            wallet: Wallet | None = Wallet.objects.filter(
                owner=req.user, pk=wallet_id
            ).first()
            if wallet is None:
                return write_json_response(404, 'Wallet not found')

            transactions = list(
                map(
                    map_transaction,
                    list(
                        Transaction.objects.select_related('wallet')
                        .filter(actor=req.user, wallet=wallet)
                        .order_by('-done_on', '-id')
                    ),
                )
            )

        key_fn = lambda trx: trx['done_on']
        transactions_map_by_date = itertools.groupby(transactions, key_fn)

        transactions = []
        for date, trxs in transactions_map_by_date:
            transactions.append({'date': date, 'transactions': list(trxs)})

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
def transaction_detail_page(req: HttpRequest, id: int) -> HttpResponse:
    if req.method == "GET":
        transaction: Transaction | None = (
            Transaction.objects.select_related('wallet')
            .filter(pk=id, actor=req.user)
            .first()
        )
        if transaction is None:
            return write_json_response(404, 'Transaction not found')

        transaction_obj = model_to_dict(transaction)
        transaction_obj["done_on"] = str(transaction_obj["done_on"])
        transaction_obj["wallet"] = model_to_dict(transaction.wallet)

        return render(
            req, "wallet/transaction-detail.html", {'transaction': transaction_obj}
        )

    return write_json_response(405, 'Method not allowed')


@login_required(login_url='/authentication/login')
def transaction_detail(req: HttpRequest, id: int) -> HttpResponse:
    if req.method == "GET":
        transaction: Transaction | None = (
            Transaction.objects.select_related('wallet')
            .filter(actor=req.user, pk=id)
            .first()
        )
        if transaction is None:
            return write_json_response(404, 'Transaction not found')

        transaction_obj = model_to_dict(transaction)
        transaction_obj["done_on"] = str(transaction_obj["done_on"])
        transaction_obj["wallet"] = model_to_dict(transaction.wallet)

        return write_json_response(200, transaction_obj)

    elif req.method == "PUT":
        transaction: Transaction | None = (
            Transaction.objects.select_related('wallet')
            .filter(actor=req.user, pk=id)
            .first()
        )
        if transaction is None:
            return write_json_response(404, 'Transaction not found')

        wallet: Wallet = transaction.wallet
        data = json.loads(req.body)

        prev_amount = transaction.amount
        prev_t_type = transaction.type

        transaction.description = data["description"]
        transaction.amount = data["amount"]
        transaction.done_on = data["done-on"]
        transaction.type = data["type"]

        transaction.save()

        amount = float(data["amount"])
        amount_diff = abs(amount - prev_amount)
        t_type = transaction.type

        if t_type == TransactionType.INCOME:
            if prev_t_type == TransactionType.INCOME:
                if amount > prev_amount:
                    wallet.balance += amount_diff
                else:
                    wallet.balance -= amount_diff
            else:
                wallet.balance += prev_amount + amount

        else:
            if prev_t_type == TransactionType.OUTCOME:
                if amount > prev_amount:
                    wallet.balance -= amount_diff
                else:
                    wallet.balance += amount_diff
            else:
                wallet.balance -= prev_amount + amount

        wallet.save()

        return redirect('wallet:transaction-detail', id=id)

    elif req.method == "DELETE":
        transaction: Transaction | None = (
            Transaction.objects.select_related('wallet')
            .filter(actor=req.user, pk=id)
            .first()
        )
        if transaction is None:
            return write_json_response(404, 'Transaction not found')

        wallet: Wallet = transaction.wallet

        if transaction.type == TransactionType.INCOME:
            wallet.balance -= transaction.amount
        else:
            wallet.balance += transaction.amount

        wallet.save()
        transaction.delete()

        return redirect('wallet:transactions')

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
