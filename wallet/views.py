import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from wallet.helpers import write_json_response
from wallet.models import Wallet

# Create your views here.
@login_required(login_url='/authentication/login')
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'wallet/index.html')


@login_required(login_url='/authentication/login')
def create_wallet(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, 'wallet/create-wallet.html')

    elif request.method == "POST":
        data = json.loads(request.body)

        Wallet.objects.create(
            owner=request.user,
            name=data["name"],
            description=data["description"],
            balance=data["initial-balance"],
        )

        return redirect("wallet:index")

    return write_json_response(405, 'Method not allowed')
