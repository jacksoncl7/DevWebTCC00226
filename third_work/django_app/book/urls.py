from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('prod/<int:id>', views.prod, name='prod')
]
