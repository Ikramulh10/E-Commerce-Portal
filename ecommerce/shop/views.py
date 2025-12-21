from decimal import Decimal
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Customer, Product, Order, OrderItem

TAX_RATE = Decimal('0.05')


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
    products = Product.objects.all()
    return render(request, 'product_list.html', {
        'products': products
    })


@login_required
def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
            stock=request.POST.get('stock'),
            image=request.FILES.get('image')
        )
        return redirect('/products/')
    return render(request, 'product_add.html')


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        pid = str(request.POST.get('product_id'))
        qty = int(request.POST.get('quantity', 1))

        if pid in cart:
            cart[pid] += qty
        else:
            cart[pid] = qty

        request.session['cart'] = cart
        request.session.modified = True

    return redirect('/products/')


@login_required
def remove_from_cart(request, pid):
    cart = request.session.get('cart', {})
    if str(pid) in cart:
        del cart[str(pid)]
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('/cart/')


@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    items = []
    subtotal = Decimal('0.00')

    for pid, qty in cart.items():
        product = Product.objects.get(id=int(pid))
        sub = product.price * qty
        subtotal += sub
        items.append({
            'product': product,
            'quantity': qty,
            'subtotal': sub
        })

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

    subtotal = Decimal('0.00')
    for pid, qty in cart.items():
        product = Product.objects.get(id=int(pid))
        subtotal += product.price * qty

    tax = subtotal * TAX_RATE
    total = subtotal + tax

    order = Order.objects.create(
        customer=customer,
        total_price=total
    )

    for pid, qty in cart.items():
        product = Product.objects.get(id=int(pid))
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=qty,
            price=product.price
        )
        product.stock -= qty
        product.save()

    request.session['cart'] = {}
    request.session.modified = True

    return render(request, 'success.html', {'order': order})


@login_required
def order_history(request):
    orders = request.user.customer.order_set.all()
    return render(request, 'orders.html', {
        'orders': orders
    })
