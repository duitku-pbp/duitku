from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
@login_required(login_url='/authentication/login')
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')
