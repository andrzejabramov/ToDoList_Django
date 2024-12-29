from django.db import models
from django.db.models import Model


class TodoItem(models.Model):
    text = models.CharField(max_length=50, null=False)
    done = models.BooleanField(null=False, default=False)