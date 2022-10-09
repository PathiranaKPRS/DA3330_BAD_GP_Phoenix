from re import U
from django.shortcuts import redirect, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def contactus(request):
    return render(request,'contactus.html')

def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'home.html')

def index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')

def login(request):
    error = ""
    if request.method =="POST":
        u=request.POST['username']
        p=request.POST['password']
        user =authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request, user)
                error="No"
            else:
                error="yes"

        except:
            error="yes"
    d = {'error':error}
    return render(request,'logins.html',d)

def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    
    logout(request)
    return redirect('login')