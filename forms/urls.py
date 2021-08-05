from django.urls import path

from .views import list,create, update, delete

urlpatterns = [
    path("", list, name="product-list"),
    path("create/", create, name="product-create"),
    path("update/<int:pk>/", update, name="product-update"),
    path("delete/<int:pk>/", delete, name="product-delete"),
]