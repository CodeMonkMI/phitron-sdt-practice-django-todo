from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from todo.forms import TodoCreateFrom
from todo.models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.filter().order_by("created_at")
    context = {"todos": todos}
    return render(request, "all.html", context)


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


def single(request, id):

    try:
        todo = Todo.objects.get(pk=id)

        context = {"todo": todo}
        return render(request, "single.html", context)
    except Todo.DoesNotExist:
        return render(request, "single.html")


def update(request, id):

    try:
        todo = Todo.objects.get(pk=id)
        if request.method == "POST":
            form = TodoCreateFrom(request.POST, instance=todo)
            if form.is_valid():
                form.save()
                context = {
                    "isFound": True,
                    "form": form,
                    "todo": todo,
                    "id": id,
                    "message": "Todo updated successfully",
                }
                return render(request, "update.html", context)

        form = TodoCreateFrom(instance=todo)
        context = {
            "isFound": True,
            "form": form,
            "id": id,
            "todo": todo,
        }
        return render(request, "update.html", context)
    except Todo.DoesNotExist:
        return render(request, "update.html")


def delete(request, id):
    try:
        todo = get_object_or_404(Todo, id=id)

        if request.method == "POST":
            todo.delete()

        return redirect("index")
    except Todo.DoesNotExist:
        return redirect("index")
