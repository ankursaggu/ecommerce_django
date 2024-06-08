from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, Product, Cart, CartProduct
from django.contrib.auth.decorators import login_required
from .recommender import recommend_products

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    recommended_ids = recommend_products(product_id)
    recommended_products = Product.objects.filter(id__in=recommended_ids)
    return render(request, 'store/product_detail.html', {'product': product, 'recommended_products': recommended_products})

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'store/cart_detail.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
    cart_product.quantity += 1
    cart_product.save()
    return redirect('cart_detail')

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    order = Order.objects.create(user=request.user, total_price=0)
    total_price = 0
    for cart_product in cart.cartproduct_set.all():
        order.products.add(cart_product.product)
        total_price += cart_product.product.price * cart_product.quantity
    order.total_price = total_price
    order.save()
    cart.delete()  # Clear the cart
    return render(request, 'store/checkout.html', {'order': order})
