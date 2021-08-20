from django.db import models
from django.db.models.fields import CharField



class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to = "media/images", null=True)
    slug = models.CharField(max_length=255, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = "media/images", null=True)
    slug = models.CharField(max_length=255, null=True)
    price = models.FloatField(default=5000)
    is_active = models.BooleanField(default=True)
      

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



# class Actor(models.Model):
#     fullname = models.CharField(max_length=255)
#     age = models.PositiveIntegerField(default=0)

#     def __str__(self):
#         return self.fullname


# class Movie(models.Model):
#     title  = models.CharField(max_length=255)
#     release_data = models.DateTimeField()
#     Actors = models.ManyToManyField(Actor)

#     def __str__(self):
#         return self.title

