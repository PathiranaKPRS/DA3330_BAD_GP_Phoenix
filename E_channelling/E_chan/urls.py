#from .import views
from django.urls import path
from .views import about,home,contactus,register_request,login_request,logout_request,appointment

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contactus/',contactus,name='contactus'),
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name= "logout"),
    path("appointment/", appointment, name="appointment"),
#     path("doctorlist/", doctorlist, name="doctorlist"),
]
