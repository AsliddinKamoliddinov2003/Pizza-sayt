from django.urls import path
from .views import  index_views



urlpatterns = [
    path("", index_views, name="bosh-sahifa"),
]