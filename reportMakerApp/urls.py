from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.logIn, name='login'),
    path('logout/', views.logOut, name='logout'),
    path('signup/', views.signUp, name='signup'),
    path('test/', views.test, name='test'),
    path('home/', views.home, name='home'),
    path('login', lambda req:redirect('login')),
    path('signup', lambda req:redirect('signup')),
    path('test', lambda req:redirect('test')),
    path('home', lambda req:redirect('home')),
]