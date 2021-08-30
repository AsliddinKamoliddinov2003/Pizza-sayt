from django.urls import path

from .views import contact, register_user, login_user


urlpatterns = [
    path("contact/", contact, name="contact"),
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login-user")
]