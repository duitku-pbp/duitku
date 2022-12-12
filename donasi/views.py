from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from donasi.models import Donasi
from donasi.forms import addNewDonasi
import json

@login_required(login_url='/authentication/login/')
def show_ajax(request):
    return render(request, "donasi_ajax.html")

def add_donasi_list(request):
    if request.method == "POST":
        form = addNewDonasi(request.POST)
        if form.is_valid():
            data = Donasi(
                user = request.user,
                date = datetime.datetime.now(),
                name = form.cleaned_data["Nama"],
                amount = form.cleaned_data["Nominal"],
                target = form.cleaned_data["Tujuan"]
            )
            data.save()
            return redirect('donasi:list_donasi')

    form = addNewDonasi()
    context = {'form':form}
    return render(request, 'addDonasi.html', context)

def show_json(request):
    donasi_list = Donasi.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', donasi_list))

def add_donasi_ajax(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_donasiList = Donasi(
            user=request.user, 
            name=data["name"], 
            amount=data["amount"], 
            target=data["target"], 
            date=data["date"],
            )

        new_donasiList.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def show_ajax(request):
    return render(request, "donasi_ajax.html")

def submitDonasi_ajax(request, id):
    donasi_list = Donasi.objects.filter(user=request.user).get(pk=id)
    donasi_list.delete()

    return HttpResponse(b"DELETED", status=204)