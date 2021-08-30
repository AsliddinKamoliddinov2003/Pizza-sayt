from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.hashers import make_password


from .models import Contact, User


class UserContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "surname", "phone_number", "gmail", "message"]


    def __init__(self, *args, **kwargs):
        super(UserContactForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].widget.attrs["placeholder"] = f"Your {field}"

        self.fields["gmail"].widget.attrs["type"] = "gmail"


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields  = ["name", "surname", "gmail", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].widget.attrs["placeholder"] = f"Your {field}"

        self.fields["gmail"].widget.attrs["type"] = "gmail"

    def save(self, *args, **kwargs):
        password1 = self.cleaned_data.pop("password1")
        password2 = self.cleaned_data.pop("password2")
        print(password1, password2)

        if password1 == password2:
            super(UserRegisterForm, self).save(*args, **kwargs)
            user = User.objects.get(gmail = self.cleaned_data["gmail"])
            user.set_password(password1)
            user.save()


class UserLoginForm(forms.Form):
    gmail = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].widget.attrs["placeholder"] = f"Your {field}"

