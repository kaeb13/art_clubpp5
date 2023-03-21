from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Poster
from django.db.models import Q
from products.models import Artist, Poster



# Create your views here.


def all_products(request):
    """ A view to show all products including sorting and search queries """

    products = Poster.objects.all()
    query = None
    sort = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(title__icontains=query) | Q(artist__name__icontains=query)
            products = products.filter(queries)

        if 'sort' in request.GET:
            sort = request.GET['sort']
            if sort == 'artist':
                products = products.order_by('artist__name')
            elif sort == 'format':
                products = products.order_by('format_type')

        if 'new_arrivals' in request.GET:
            new_arrivals = request.GET['new_arrivals']
            if new_arrivals == 'true':
                products = products.filter(is_new_arrival=True)

    context = {
        'products': products,
        'search_term': query,
        'sort': sort,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, pk):
    """ A view to show the details of a single product """
    product = get_object_or_404(Poster, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    poster = get_object_or_404(Poster, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)  

