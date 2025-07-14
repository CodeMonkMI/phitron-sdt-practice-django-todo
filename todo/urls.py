from django.urls import path


from todo.views import index, create, delete, single, update

urlpatterns = [
    path("", index, name="index"),
    path("create/", create, name="create"),
    path("<uuid:id>/", single, name="single"),
    path("<uuid:id>/update/", update, name="update"),
    path("<uuid:id>/delete/", delete, name="delete"),
]
