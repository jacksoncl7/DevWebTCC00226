from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from book.models import Book

def index(request):
    books = Book.objects.all()
    context = {'books' : books}
    return render(request, 'book/index.html', context)

def prod(request, id):
    book = Book.objects.get(pk=id)
    context = {'book' : book}
    return render(request, 'book/product.html', context)

def cart(request):
    prods = ('here may has','a lot of ', 'objects')
    return render(request, 'book/cart.html', { 'cart' : prods } )
