from django.shortcuts import render

# Create your views here.

def throw(request):
    return render(request, 'first/throw.html')

def catch(request):
    msg = request.GET.get('msg')

    context = {
        'msg': msg
    }
    return render(request, 'first/catch.html', context)