from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')


def fake_google(request):
    return render(request, 'pages/fake-google.html')


def introduce(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'pages/introduce.html', context)


# 사용자 정보를 입력받는 throw.html 렌더링
def throw(request):
    return render(request, 'pages/throw.html')


# 사용자 정보를 받아서 처리하는 로직
def catch(request):

    # throw를 통해 전달한 정보를 꺼낸다.
    content = request.GET.get('content')

    context = {
        'content': content,
    }

    return render(request, 'pages/catch.html', context)