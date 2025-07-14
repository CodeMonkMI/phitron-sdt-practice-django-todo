from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from todo.forms import TodoCreateFrom

# Create your views here.


def index(request):
    return render(request, "all.html")


def create(request: HttpRequest):

    if request.method == "POST":
        form = TodoCreateFrom(request.POST)
        context = {"message": "Todo creation failed successfully!", "form": form}

        if form.is_valid():
            form.save()
            context["message"] = "Todo created successfully!"
        return render(request, "create.html", context)

    form = TodoCreateFrom()
    context = {"form": form}
    return render(request, "create.html", context)


def single(request):
    return render(request, "single.html")


def update(request):
    return render(request, "update.html")


def delete(request):
    return render(request, "all.html")
