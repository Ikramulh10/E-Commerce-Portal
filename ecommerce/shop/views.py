from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Customer, Product, Order, OrderItem

TAX_RATE = 0.05

def signup_view(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['email'],
            email=request.POST['email'],
            password=request.POST['password'],
            first_name=request.POST['name']
        )
        Customer.objects.create(user=user)
        login(request, user)
        return redirect('/products/')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['email'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('/products/')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required
def product_list(request):
    return render(request, 'product_list.html', {
        'products': Product.objects.all()
    })

@login_required
def add_to_cart(request):
    cart = request.session.get('cart', {})
    pid = request.POST['product_id']
    qty = int(request.POST['quantity'])
    cart[pid] = cart.get(pid, 0) + qty
    request.session['cart'] = cart
    return redirect('/products/')

@login_required
def remove_from_cart(request, pid):
    cart = request.session.get('cart', {})
    cart.pop(str(pid), None)
    request.session['cart'] = cart
    return redirect('/cart/')

@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    items, subtotal = [], 0

    for pid, qty in cart.items():
        product = Product.objects.get(id=pid)
        sub = product.price * qty
        subtotal += sub
        items.append({'product': product, 'quantity': qty, 'subtotal': sub})

    tax = subtotal * TAX_RATE
    total = subtotal + tax

    return render(request, 'cart.html', {
        'items': items,
        'subtotal': subtotal,
        'tax': tax,
        'total': total
    })

@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    customer = request.user.customer

    subtotal = sum(
        Product.objects.get(id=pid).price * qty
        for pid, qty in cart.items()
    )
    total = subtotal + (subtotal * TAX_RATE)

    order = Order.objects.create(customer=customer, total_price=total)

    for pid, qty in cart.items():
        product = Product.objects.get(id=pid)
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=qty,
            price=product.price
        )
        product.stock -= qty
        product.save()

    request.session['cart'] = {}
    return render(request, 'success.html', {'order': order})

@login_required
def order_history(request):
    return render(request, 'orders.html', {
        'orders': request.user.customer.order_set.all()
    })
