from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from book.models import Book

def index(request):
    books = Book.objects.all()
    context = {'book' : books}
    return render(request, 'book/index.html', context)

def prod(request):
    prod = ('uniqueProduct')
    return render(request, 'book/product.html', {'product' : prod})

def cart(request):
    prods = ('here may has','a lot of ', 'objects')
    return render(request, 'book/cart.html', { 'cart' : prods } )
