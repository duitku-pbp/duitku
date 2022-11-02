from sre_constants import IN
from unicodedata import name
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from investasiku.models import Investment, Portofolio
from wallet.models import Wallet, Transaction, TransactionType
# Create your views here.
def show_landing_page(request):
    return render(request, "landing.html")

def show_investment_all(request):
    context = {
        'filter' : 'All'
    }
    return render(request, "investment_list.html", context)
def show_investment_pasaruang(request):
    context = {
        'filter' : 'Pasar Uang'
    }
    return render(request, "investment_list.html", context)

def show_investment_obligasi(request):
    context = {
        'filter' : 'Obligasi'
    }
    return render(request, "investment_list.html", context)

def show_investment_saham(request):
    context = {
        'filter' : 'Saham'
    }
    return render(request, "investment_list.html", context)

# @login_required(login_url='/authentication/login/')
def show_app(request):
    return render(request, "app.html")

def add_portofolio(request):
    if request.method == 'POST':
        pk_item = request.POST.get("pk")
        investation = Portofolio(user=request.user,bought_value= request.POST.get("jumlah_beli"),investment = Investment.objects.filter(pk=pk_item).first())
        investation.save()
        
        investment = Investment.objects.filter(pk=pk_item).first().investment_name
        wallet = Wallet(
            owner=request.user,
            name=investment + " | Investasi Reksa Dana @Investasiku",
            description="Investasi Reksadana Sejumlah " + request.POST.get("jumlah_beli"),
            balance= request.POST.get("jumlah_beli"),
        )
        wallet.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def purge_portofolio(request):
    Portofolio.objects.all().delete()
    return show_app(request)

def show_json_all(request):
    data = Investment.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_json_pasaruang(request):
    data = Investment.objects.filter(investment_type="Pasar Uang")
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_json_obligasi(request):
    data = Investment.objects.filter(investment_type="Obligasi")
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_json_saham(request):
    data = Investment.objects.filter(investment_type="Saham")
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_json_id(request, id):
    data = Investment.objects.get(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_portofolio(request):
    data = Portofolio.objects.filter(user = request.user)
    
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")