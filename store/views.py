from django.db.models.fields import CharField
from django.shortcuts import get_object_or_404, render
from django.views.generic import DeleteView


from forms.models import  Category, Product



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


