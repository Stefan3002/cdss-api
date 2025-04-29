from django.db import models
from django.db.models import Model


# Create your models here.

class Widget(Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    downloads = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name