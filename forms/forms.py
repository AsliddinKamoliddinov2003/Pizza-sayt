from django import forms
from django.db.models import fields


from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"



    def __init__(self, *args, **kwargs):
        super(ProductForm,self).__init__(*args, **kwargs)


        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

        def __init__(self, *args, **kwargs):
            super(ProductForm,self).__init__(*args, **kwargs)


            for field in self.fields:
                self.fields[field].widget.attrs["class"] = "form-control"

