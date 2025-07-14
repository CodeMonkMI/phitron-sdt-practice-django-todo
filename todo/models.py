from django.db import models


# Create your models here.
class Todo(models.Model):
    id = models.UUIDField(primary_key=True)
    text = models.CharField()
    description = models.TextField()
    meta = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
