from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Poster
from django.db.models import Q

# Create your views here.


def all_products(request):
    """ A view to show all products including sorting and search queries """

    products = Poster.objects.all()
    query = None
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(title__icontains=query) | Q(artist__name__icontains=query)
            products = products.filter(queries) 
            

    context = {
        'products': products,
        'search_term': query,
        
    }

    return render(request, 'products/products.html', context)

    
def product_detail(request, pk):
    """ A view to show the details of a single product """
    product = get_object_or_404(Poster, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)