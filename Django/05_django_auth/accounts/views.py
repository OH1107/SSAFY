from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomUserChangeForm


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            # 세션 CREATE
            auth_login(request, form.get_user())
            # 만약 next 파라미터가 있으면 next로 보내고 없으면 articles:index로 보낸다.
            return redirect(request.GET.get('next') or 'articles:index')
            
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if reqeust.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST': # 회원가입 후 로그인
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # user instance 반환
            auth_login(request, user) # 로그인
            return redirect('articles:index') # 홈으로
    else: # GET 회원가입 form 제공
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        auth_logout(request) # 회원 로그아웃 해서 세션 제거
        request.user.delete() # 탈퇴 (DB에서 제거)
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)