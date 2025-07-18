from .views import *
from django.urls import path

urlpatterns = [
    path('cleopatra/', cleopatra, name="cleopatra"),
    path('movies/', movies, name="movies"),
]