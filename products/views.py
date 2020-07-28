from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def all_products(request):
    """ A view to return all products, searches and filtering of the  Product page """

    products = Product.objects.all()
    context = {
        'products': products,
    }
    paginator = Paginator(products, 15)
    page = request.GET.get('page')
    
    return render(request, 'products/products.html', context)
