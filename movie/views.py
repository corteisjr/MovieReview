from django.shortcuts import render
from django.http import HttpResponse
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

def about(requet):
    return HttpResponse("<h1>About us</h1>")

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

