from django.shortcuts import render


from forms.models import Product, Category



def index_views(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        "products": products,
        "categories":categories
    }

    return render(request, "index.html", context)
