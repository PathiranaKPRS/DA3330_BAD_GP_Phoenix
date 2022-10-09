
from django.urls import path
from .views import about,home,contactus

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contactus/',contactus,name='contactus')
]    
