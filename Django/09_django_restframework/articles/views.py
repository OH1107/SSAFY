from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer


# 페이지가 목적이 아닌, 데이터가 목적!
@api_view(['GET', 'POST'])
def articles(request):
    if request.method == 'GET':
        # article 목록을 가져온다, 없으면 404를 응답
        article_list = get_list_or_404(Article)
        serializer = ArticleListSerializer(article_list, many=True)
        return Response(serializer.data)
    else:
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 201 Created
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    else:   # DELETE
        article.delete()
        response = {'pk': pk}
        return Response(response, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def comments(request):
    comment_list = get_list_or_404(Comment)
    serializer = CommentSerializer(comment_list, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    else:
        comment.delete()
        response = {'pk': pk}
        return Response(response, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def article_comments(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        comment_list = article.comment_set.all()
        # comment_list = get_list_or_404(Comment, article=article)
        serializer = CommentSerializer(comment_list, many=True)
        return Response(serializer.data)

    else:
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data)