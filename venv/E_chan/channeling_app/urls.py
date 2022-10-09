
from django.urls import path
from .views import about,home,contactus,login

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contactus/',contactus,name='contactus'),
    path('admin_login/',login,name='login'),
]    
