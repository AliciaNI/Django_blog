from django.shortcuts import render

from post.models import Article, Comment


def home(request):
    articles = Article.object.all()
    return render(request, 'home.html', {'articles': articles})


def detail(request):
    aid = int(request.GET.get('aid'))
    article = Article.object.get(aid)
    return render(request, 'detail.html', {'article': article})


def edit(request):
    return render(request, '', {})


def delete(request):
    return render(request, '', {})


def search(request):
    return render(request, '', {})
