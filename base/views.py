from django.shortcuts import render

# Create your views here.
def Home(request):
    context = {}
    return render(request, 'letstalk/main.html', context)

def Login(request):
    context = {}
    return render(request, 'letstalk/login.html', context)
