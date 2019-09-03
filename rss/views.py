from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import NewsFeed
import feedparser

def rss_view(request):
    news_feed = NewsFeed.objects.all()
    return render(request, 'rss.html', {'news_feed': news_feed})

def search_url(request):
    u = request.POST['url_input']
    
    new_url_feedparse = feedparser.parse(u)
    new_url_entries = new_url_feedparse.entries
    new_url = NewsFeed(url_input = new_url_entries)
    new_url.save()
    print(new_url_entries)

    context = {
        'url_entries': new_url_entries
    }
    
    #return HttpResponseRedirect('/rss/')
    return render(request, 'rss.html', context)


    
