from django.contrib.admin.helpers import ActionForm
from django.db.models.base import Model
from forms.models import  Category,  Product
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "category", "is_active"]
    list_editable = [ "price", "category", "is_active"]
    search_fields = ["title", "description"]
    prepopulated_fields = {"slug":("title",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)