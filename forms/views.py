from django.shortcuts import redirect, render
from django.urls import reverse


from .models import Product, Category


def list(request):
    products = Product.objects.all()
    context = {
        "products": products
    }

    return render(request, "forms/list.html", context)


def create(request):
    if request.method == "POST":
        title = request.POST.get("title", None)
        description = request.POST.get("description", None)
        category_id = request.POST.get("category_id", None)
    
        category = Category.objects.get(id=category_id)

        p = Product()
        p.title = title
        p.description = description
        p.category = category

        p.save()

        return redirect(reverse("product-list"))

    categories = Category.objects.all()
    context = {
        "categories": categories
    }


    return render(request, "forms/create.html", context)


def update(request, pk):
    product = Product.objects.filter(id=pk)

    if not product.exists():
        return redirect(reverse("product-list"))
    else:
        product=product.first()

    if request.method == "POST":
        title = request.POST.get("title", None)
        description = request.POST.get("description", None)
        category_id = request.POST.get("category_id", None)
    
        category = Category.objects.get(id=category_id)
        
        product.title = title
        product.description = description
        product.category = category

        product.save()

        return redirect(reverse("product-list"))

    categories = Category.objects.all()
    context = {
        "categories": categories,
        "product":product
    }
    return render(request, "forms/update.html", context)


def delete(request,pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
    except Product.DoesNotExist:
        pass
    return redirect(reverse("product-list"))