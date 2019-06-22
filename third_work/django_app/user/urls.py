from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('log', views.log, name='login'),
]
