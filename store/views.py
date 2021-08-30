from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required


from forms.models import  Category, Product
from .forms import *
from .models import *



@login_required(login_url="account/login/")
def index_views(request):
    categories = Category.objects.all()
    context = {
        "categories":categories
    }

    return render(request, "index.html", context)


@login_required(login_url="account/login/")
def all(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category__name = category)
    context = {
        "products":products
    }
    return render(request, "product_detail.html", context)




    





