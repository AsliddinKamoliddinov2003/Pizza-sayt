from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to = "images/", null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = "images/", null=True)
      

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

