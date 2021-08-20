from django.core.files.base import ContentFile
from forms.forms import ProductForm
from django.shortcuts import redirect, render
from django.urls import reverse


from .models import Product, Category
from .forms import *


def list(request):
    products = Product.objects.all()
    context = {
        "products": products
    }

    return render(request, "forms/list.html", context)


def create(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("product-list"))
        


    context = {
        "form":form
    }

    return render(request, "forms/create.html", context)


def update(request, pk):

    product = Product.objects.filter(id=pk)

    if not product.exists():
        return redirect(reverse("product-list"))
    else:
        product=product.first()

    form = ProductForm(instance=product)

    if request.method == "POST":
        product = ProductForm(request.POST, request.FILES, instance = product)
        if product.is_valid():
            product.save()
            return redirect(reverse("product-list"))

       

    context = {
        "form":form
    }
    return render(request, "forms/update.html", context)


def delete(request,pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
    except Product.DoesNotExist:
        pass
    return redirect(reverse("product-list"))


def category(request):

    categories = Category.objects.all()
    context = {
        "categories": categories
    }

    return render(request, "forms/category_list.html", context)


def create_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("category-list"))
        
    context = {
            "form": form
    }
    
    return render(request, 'forms/create_category.html', context)


def update_category(request, pk):

    category = Category.objects.filter(id=pk)

    if not category.exists():
        return redirect(reverse("bosh-sahifa"))
    else:
        category=category.first()

    form = CategoryForm(instance=category)

    if request.method == "POST":
        category = CategoryForm(request.POST, request.FILES, instance=category)
        if category.is_valid():
            category.save()
            return redirect(reverse("category-list"))
    
    context = {
        "form":form
    }
    
    return render(request, 'forms/update_category.html', context)
    
    
def delete_category(request, pk):
    try:
        category=Category.objects.get(id=pk)
        category.delete()
    except Category.DoesNotExist:
        pass
    return redirect(reverse('category-list'))


# def home(request):
#     actors = Movie.objects.all()
#     context = {
#         "actors":actors
#     }
#     return render(request, "forms/home.html", context)


# def create_actor(request):
#     return 


# def update_actor(request, pk):
#     return


# def delete_actor(request, pk):
#     return

