from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=255)
    gmail = models.CharField(max_length=255, unique=True)
    phone_number = models.FloatField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


