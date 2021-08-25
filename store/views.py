from django.db.models.fields import CharField
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse


from forms.models import  Category, Product
from .forms import *
from .models import *




def index_views(request):
    categories = Category.objects.all()
    context = {
        "categories":categories
    }

    return render(request, "index.html", context)



def all(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category__name = category)
    context = {
        "products":products
    }
    return render(request, "product_detail.html", context)


def contact(request):
    form = UserContactForm()

    if request.method == "POST":
        form = UserContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(reverse('bosh-sahifa'))

    

def all_contact(request):
    contacts = Contact.objects.all()

    context = {
        "contacts":contacts
    }

    return render(request, "account/client.html", context)
        

        

    





