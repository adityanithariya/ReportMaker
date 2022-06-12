from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signUp/', views.signup, name='signup'),
    path('test/', views.test, name='test'),
    path('home/', views.home, name='home'),
]