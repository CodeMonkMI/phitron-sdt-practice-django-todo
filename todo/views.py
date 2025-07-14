from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def index(request):
    return render(request, "all.html")


def create(request):
    return render(request, "create.html")


def single(request):
    return render(request, "single.html")


def update(request):
    return render(request, "update.html")


def delete(request):
    return render(request, "all.html")
