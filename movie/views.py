from .forms import ReviewForm
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Movie as Movies, Review

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
    reviews = Review.objects.filter(movie = movie)
    return render(request, 'detail.html', {'movie':movie, 'reviews':reviews})

def about(requet):
    return HttpResponse("<h1>About us</h1>")

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})


def createreview(request, movie_id):
    movie = get_object_or_404(Movies, pk=movie_id)
    if request.method == 'GET':
        return render(request, 'createreview.html', {'form':ReviewForm(), 'movie':movie})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect(
                'detail',
                newReview.movie.id
            )
            
        except:
            return render(
                'createreview.html',
                {
                    'form':ReviewForm(),
                    'error': 'bad data passed in'
                }
            )