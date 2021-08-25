from django.db.models import fields
from django import forms

from .models import Contact


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