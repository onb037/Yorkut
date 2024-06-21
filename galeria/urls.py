from django.urls import path 
from galeria.views import index, posts 

urlpatterns = [
    path('', index),
    path('card/', posts, name='card')
]