from django.shortcuts import render

from re import U
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def contactus(request):
    return render(request, 'contactus.html')


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")


def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your_name']
        your_phone = request.POST['your_phone']
        your_email = request.POST['your_email']
        your_address = request.POST['your_address']
        your_schedule = request.POST['your_schedule']
        your_date = request.POST['your_date']
        your_message = request.POST['your_message']

        return render(request, 'appoinment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_date': your_date,
            'your_message': your_message
        })

    else:
        return render(request, 'home.html', {})

def doctorlist(request):
    return render(request, 'doctorlist.html')
