from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def index(request):
    return HttpResponse("Get all todo ")


def create(request):
    return HttpResponse("Create todo ")


def single(request):
    return HttpResponse("Get single todo")


def update(request):
    return HttpResponse("Update todo todo")


def delete(request):
    return HttpResponse("Delete todo")
