from django.shortcuts import render
from .models import News
# listing news
def news(request):
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss':newss})
