from django.db import models

class Thing(models.model):
    name = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=150, blank=False)
    quantity = models.PositiveIntegerField(default=1)