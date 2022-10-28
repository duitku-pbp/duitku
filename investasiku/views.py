from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from investasiku.models import Investment
# Create your views here.
def show_landing_page(request):
    return render(request, "landing.html")

def show_pasaruang(request):
    return render(request, "pasaruang.html")

def show_obligasi(request):
    return render(request, "obligasi.html")
    
def show_saham(request):
    return render(request, "saham.html")

# @login_required(login_url='/authentication/login/')
def show_app(request):
    return render(request, "app.html")

def show_json(request):
    data = Investment.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")