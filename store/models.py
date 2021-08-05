from django.db import models


class User(models.Model):
    name = models.TextField(max_length=255)
    phone = models.CharField(max_length=255)
    gmail = models.CharField(max_length=255)
    client = models.BooleanField()
    admin = models.BooleanField()
    super_admin = models.BooleanField()
