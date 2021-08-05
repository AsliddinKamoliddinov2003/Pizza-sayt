from django.urls import path
from django.contrib import  admin
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include("store.urls")),
    path('forms/',include("forms.urls")),
]
