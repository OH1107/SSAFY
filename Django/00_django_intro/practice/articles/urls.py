from django.urls import path
from . import views

# mysite.com/articles/

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index')
]
