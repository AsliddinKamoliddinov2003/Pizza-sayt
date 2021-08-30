from django.urls import path
from django.contrib import  admin
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include("store.urls")),
    path('forms/',include("forms.urls")),
    path('account/',include("account.urls")),
]  + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
