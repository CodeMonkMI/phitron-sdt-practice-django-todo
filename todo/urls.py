from django.urls import path


from todo.views import index, create, delete, single, update

urlpatterns = [
    path("", index, name="index"),
    path("create/", create, name="create"),
    path("delete/", delete, name="delete"),
    path("single/", single, name="single"),
    path("update/", update, name="update"),
]
