from django.db import models
from django.db.models.fields import CharField


class User(models.Model):
    name = models.TextField(max_length=255)
    phone = models.CharField(max_length=255)
    gmail = models.CharField(max_length=255)
    client = models.BooleanField()
    admin = models.BooleanField()
    super_admin = models.BooleanField()


