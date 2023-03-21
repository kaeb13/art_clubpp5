from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ A view that renders the bags contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    form = BagForm(request.POST or None, initial={'product_id': item_id})
    if request.method == 'POST':
        if form.is_valid():
            bag = request.session.get('bag', {})
            quantity = form.cleaned_data['quantity']
            size = form.cleaned_data.get('size', None)
            if size:
                item_data = {'size': size, 'quantity': quantity}
            else:
                item_data = quantity
            bag[item_id] = bag.get(item_id, {})
            if size:
                if size in bag[item_id]['items_by_size'].keys():
                    bag[item_id]['items_by_size'][size] += quantity
                    messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
                else:
                    bag[item_id]['items_by_size'][size] = quantity
                    messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
            else:
                bag[item_id] = quantity
                messages.success(request, f'Added {product.name} to your bag')
            request.session['bag'] = bag
            return redirect(reverse('view_bag'))
    context = {
        'form': form,
        'product': product,
    }
    context.update(get_bag_items(request))
    return render(request, 'products/product_details.html', context)    
