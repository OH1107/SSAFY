from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm


@require_GET
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# # GET => Form을 받아감
# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


# # POST => Data 생성
# def create(request):
#     form = ArticleForm(request.POST)
#     if form.is_valid():
#         article = form.save()
#         # return redirect('articles:detail', article.pk)
#     return redirect('articles:index')


# 요청에 따라 작동하는 하나의 함수
@require_http_methods(['GET', 'POST'])
def create(request):
    # 빈 Form 렌더링
    if request.method == 'GET':
        form = ArticleForm()
        
    # 생성로직, 실패시 작성한 Form 렌더링
    else: # POST:
        form = ArticleForm(request.POST)
        # 데이터가 유효한 경우 => 생성 후 redirect
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')

    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_GET
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# # GET => 수정 페이지 렌더링
# def edit(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)


# # POST = 업데이트 로직
# def update(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     form = ArticleForm(request.POST, instance=article)
#     if form.is_valid():
#         article = form.save()

#     return redirect('articles:detail', article.pk)


@require_POST
def delete(request, pk):
    pass


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'GET':
        form = ArticleForm(instance=article)

    else: # POST:
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)

    context = {
        'form': form,
    }
    return render(request, 'articles/update.html', context)