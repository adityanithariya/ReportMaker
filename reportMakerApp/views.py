from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'signin.html')
    
def signup(req):
    context = {
        'roles':[
            ['leader', 'Team Leader'],
            ['member', 'Team Member']
        ]
    }
    return render(req, 'signup.html', context)
    
def test(req):
    return render(req, 'test.html')