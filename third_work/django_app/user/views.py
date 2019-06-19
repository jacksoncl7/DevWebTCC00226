from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


# Create your views here.
def reg(request):
    pass

def log(request):
    prods = ('Formtupple')
    return render(request, 'user/login.html', {'book' : prods})
