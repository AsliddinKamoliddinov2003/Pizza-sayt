from django.urls import path
from .views import  index_views, all



urlpatterns = [
    path("", index_views, name="bosh-sahifa"),
    path("store/<slug:category_slug>/", all, name="all-product")
]