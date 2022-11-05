from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from . import models
# Create your views here.


def loginPage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email.strip() and password:
            try:
                user = models.User.objects.get(name=email)
            except:
                return render(request, 'login/login.html')
            if user.password == password:
                return redirect('/index/')
        # print(email, password)
        return redirect('/index/')
    return render(request, 'login/login.html')


def index(request):
    pass
    return render(request, 'login/index.html')


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect('/login/')