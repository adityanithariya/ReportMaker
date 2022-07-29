from django.shortcuts import redirect
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', logIn, name='login'),
    path('logout/', logOut, name='logout'),
    path('signup/', signUp, name='signup'),
    path('test/', test, name='test'),
    path('home/', home, name='home'),
    path('srijan/', srijan, name='srijan'),
    path('reports/', reports, name='reports'),
    path('settings/', settings, name='settings'),
    path('profile/', profile, name='profile'),
    path('forgotPass/', forgotPass, name='forgotPass'),
    path('error/', errorPage, name='error'),
    path('addReport/', addReport, name='addReport'),
]

# handler404 = 'reportMakerApp.views.handler404'
# handler500 = 'reportMakerApp.views.handler500'