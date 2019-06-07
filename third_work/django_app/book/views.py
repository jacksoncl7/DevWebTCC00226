from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    book = 'AAAAAAAAAAAAAAA'
    return render(request, 'index.html', {'book':book})
