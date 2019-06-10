from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST


def index(request):
    prods = ('here may has','a lot of ', 'objects')
    return render(request, 'book/index.html', {'book' : prods})

def prod(request):
    prod = ('uniqueProduct')
    return render(request, 'product.html', {'product' : prod})

def cart(request):
    prods = ('here may has','a lot of ', 'objects')
    return render(request, 'cart.html', { 'cart' : prods } )
