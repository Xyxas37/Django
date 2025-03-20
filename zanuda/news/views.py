from django.shortcuts import render, get_object_or_404
from .models import News_post

def news_list(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

def news_detail(request, news_id):
    news = get_object_or_404(News_post, pk=news_id)
    return render(request, 'news/news_detail.html', {'news': news})




