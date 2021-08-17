from django.urls import path

from .views import *

urlpatterns = [
    path("", list, name="product-list"),
    path("create/", create, name="product-create"),
    path("update/<int:pk>/", update, name="product-update"),
    path("delete/<int:pk>/", delete, name="product-delete"),
    path("category/", category, name="category-list"),
    path("create-category/", create_category, name="create-category"),
    path("update-category/<int:pk>/", update_category, name="update-category"),
    path("delete_category/<int:pk>/", delete_category, name="delete-category")
]









# path("home/", home, name="home"),
# path("create_actor/", create_actor, name="create-actor"),
# path("update_actor/<int:pk>/", update_actor, name="update-actor"),
# path("delete_actor/<int:pk>/", delete_actor, name="delete-actor")