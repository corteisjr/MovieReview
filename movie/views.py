import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Movie as Movies

# Listing Movies
def home(request):
    searchTerm = request.GET.get('searchMovie')
    # implementing a search
    if searchTerm:
        movies = Movies.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movies.objects.all()
    return render(
        request, 
        'home.html', 
        {'searchTerm': searchTerm,
         'movies': movies  
        },
        )
    
def detail(request, movie_id):
    movie = get_object_or_404(Movies, pk=movie_id)
    return render(request, 'detail.html', {'movie':movie})

def about(requet):
    return HttpResponse("<h1>About us</h1>")

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

