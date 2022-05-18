from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'signin.html')
    
def signup(req):
    return render(req, 'signup.html')