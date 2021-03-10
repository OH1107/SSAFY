from django.shortcuts import render, redirect
from .models import Article


# Article 목록을 보여주는 페이지
def index(request):
    articles = Article.objects.all() # QuerySet

    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html', context)


# Article 생성 폼 제공하는 페이지 렌더링
def new(request):
    return render(request, 'articles/new.html')


# new/에서 전달받은 form data를 꺼내서,
# 새로운 article을 생성
def create(request):
    # 전달 받은 form data를 꺼냄
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 새로운 article data 생성
    article = Article()
    article.title = title
    article.content = content
    article.save()

    # 사용자를 목록페이지로 보내줌
    return redirect('articles:index')