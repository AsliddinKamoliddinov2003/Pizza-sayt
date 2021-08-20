from forms.models import Product, Category


def category_context(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return {
        "categories":categories,
        "products":products
    }