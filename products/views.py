from django.shortcuts import render
from .models import Poster

# Create your views here.


def allproducts(request):
    """ A view to show all products including sorting and search quieres """

    products = Poster.objects.all()

    context = {
        'products': products,

    }
 
    return render(request, 'products/products.html', context)
