from django.contrib.admin.helpers import ActionForm
from django.db.models.base import Model
from forms.models import  Category,  Product
from django.contrib import admin


admin.site.register(Category)
admin.site.register(Product)