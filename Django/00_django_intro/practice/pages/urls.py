# mysite.com/pages/ 로 들어옴

from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    # views.py/index() => templates/index.html
    path('', views.index, name='index'),
    path('fake-google/', views.fake_google, name='fake-google'),
    path('introduce/<str:name>/<int:age>/', views.introduce, name='introduce'),

    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
]
