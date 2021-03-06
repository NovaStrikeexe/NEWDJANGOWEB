from django.shortcuts import render
from .models import Article, Comment
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def index(request):
    latest_articles_list = Article.objects.order_by('-publishing_date')[:10]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Artile not found :(")

    latest_comments_list = a.comment_set.order_by('-article_id')[:5]
    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Artile not found :(")

    Comment.objects.create(
        article=a,
        author_name=request.POST.get('name'),
        comment_text=request.POST.get('text')
    )
    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))
