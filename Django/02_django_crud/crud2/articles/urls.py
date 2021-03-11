from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # mysite.com/articles/ => 목록 페이지
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # mysite.com/articles/1/ => 디테일 페이지
    path('<int:pk>/', views.detail, name='detail'),

    # mysite.com/articles/delete/1/ => 게시글 삭제
    path('delete/<int:pk>/', views.delete, name='delete'),

    # mysite.com/articles/edit/1/
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('update/<int:pk>/', views.update, name='update'),
]
