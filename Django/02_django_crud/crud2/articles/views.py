from django.shortcuts import render, redirect, get_object_or_404
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
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 새로운 article data 생성
    article = Article()
    article.title = title
    article.content = content
    article.save()

    # 사용자를 목록페이지로 보내줌
    return redirect('articles:detail', article.pk)


def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    print(request.method)
    if request.method == 'POST':
        # pk 값으로 article을 찾는다.
        article = get_object_or_404(Article, pk=pk)

        # article을 삭제한다.
        article.delete()

    # 목록 페이지로 연결
    return redirect('articles:index')


def edit(request, pk):
    # pk 값으로 article을 찾는다.
    article = get_object_or_404(Article, pk=pk)
    
    # context 로 article 값을 template에 전달한다.
    context = {
        'article': article,
    }

    # edit.html(게시글 수정 페이지)를 렌더링한다.
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    # pk 값으로 article을 찾는다.
    article = get_object_or_404(Article, pk=pk)

    # 수정할 내용을 request.GET에서 꺼낸다.
    # article에 수정할 내용을 적용하고 저장한다.
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    # Detail 페이지로 이동한다.
    return redirect('articles:detail', pk)
