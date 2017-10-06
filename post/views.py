from django.shortcuts import render, redirect

from post.models import Article, Comment


def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})


def detail(request):
    aid = int(request.GET.get('aid'))
    article = Article.objects.get(id=aid)
    comments = Comment.objects.filter(aid=aid)
    return render(request, 'detail.html',
                  {'article': article, 'comments': comments})


def edit(request):
    if request.method == "GET":
        aid = int(request.GET.get('aid'))
        article = Article.objects.get(id=aid)
        return render(request, 'edit.html', {"article": article})
    else:
        aid = int(request.POST.get('aid'))
        content = request.POST.get('content')
        article = Article.objects.get(id=aid)
        article.content = content
        article.save()
        return redirect('/post/detail/?aid=%s' % aid)


def delete(request):
    aid = int(request.GET.get('aid'))
    article = Article.objects.get(id=aid)
    article.delete()
    return redirect('/post/home/')


def search(request):
    keyword = request.POST.get('keyword')
    articles = Article.objects.filter(title__icontains=keyword)

    return render(request, 'home.html', {'articles': articles})


def comment(request):
    aid = int(request.POST.get('aid'))
    name = request.POST.get('name')
    comment = request.POST.get('comment')

    Comment.objects.create(aid=aid, name=name, content=comment)
    return redirect('/post/detail/?aid=%s' % aid)
