from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def registration_page(request):
    return render(request, 'register.html', {})

def login_page(request):
    return render(request, 'login.html', {})

def account(request):
    return render(request, 'account.html', {})

def shop(request):
    return render(request, 'tienda.html', {})

# Ésta va a tener que ser por renderización dinámica - cada producto tiene su propio número de código.
def product(request):
    return render(request, 'product.html', {})

def cart(request):
    return render(request, 'cart.html', {})

def product(request):
    return render(request, 'product.html', {})

def cart(request):
    return render(request, 'cart.html', {})

def about_us(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})


# Error Management/Handling

def error_page(request, exception):
    return render(request, '404.html', status=404)