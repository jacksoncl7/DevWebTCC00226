from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('home', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('prod', views.prod, name='prod')
]
