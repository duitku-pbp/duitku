from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from wallet.helpers import write_json_response

# Create your views here.
@login_required(login_url='/authentication/login')
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'wallet/index.html')


@login_required(login_url='/authentication/login')
def create_wallet(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, 'wallet/create-wallet.html')

    elif request.method == "POST":
        pass

    return write_json_response(405, 'Method not allowed')
