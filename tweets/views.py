from django.shortcuts import render

from tweets.models import Book, Movies


# Create your views here.
def cleopatra(request):
    books = Book.objects.all()
    context = {
        'Books': books,
    }
    return render(request, 'cleopatra.html', context)

def movies(request):
    movies = Movies.objects.all()
    context = {
        'Movies': movies,
    }
    return render(request, 'quincy.html', context)