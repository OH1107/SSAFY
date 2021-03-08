from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def mylist(request):
    students = [
        '김싸피',
        '이싸피',
        '박싸피',
    ]
    context = {
        'students': students,
    }
    return render(request, 'mylist.html', context)