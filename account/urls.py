from django.urls import path

from .views import all_contact, contact, register_user, login_user, delete_contact


urlpatterns = [
    path("contact/", contact, name="contact"),
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login-user"),
    path("all/contacts/", all_contact, name="all-contacts"),
    path("delete/contact/<int:pk>/", delete_contact, name="delete-contact"),
]