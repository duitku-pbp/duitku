from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
def test(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello')
