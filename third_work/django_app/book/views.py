from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    prods = ('here may has','a lot of ', 'objects')
    return render(request, 'book/index.html', {'book' : prods})

def product(request):
    prod = ('uniqueProduct')
    return render(request, 'product.html', {'product' : prod})

def cart(request):
    prods = ('here may has','a lot of ', 'objects')
    return render(request, 'cart.html', { 'cart' : prods } )
