from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from shop.models import Product
from .cart import Cart


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()

    return render(
        request,
        "cart_summary.html",
        {
            "cart_products": cart_products,
            "quantities": quantities
        }
    )


def cart_add(request):

    cart = Cart(request)

    if request.method == "POST":

        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)

        cart.add(
            product=product,
            quantity=product_qty
        )

        messages.success(request, "Product added to the cart")

        # Redirect to cart page
        return redirect('cart_summary')

    return JsonResponse({
        'error': 'Invalid request method'
    }, status=400)


def cart_update(request):

    cart = Cart(request)

    if request.method == "POST":

        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)

        cart.update(
            product=product,
            quantity=product_qty
        )

        messages.success(request, "Cart updated")

        return redirect('cart_summary')

    return redirect('cart_summary')


def cart_delete(request):

    cart = Cart(request)

    if request.method == "POST":

        product_id = int(request.POST.get('product_id'))

        product = get_object_or_404(Product, id=product_id)

        cart.delete(product)

        messages.success(request, "Product removed from cart")

        return redirect('cart_summary')

    return redirect('cart_summary')