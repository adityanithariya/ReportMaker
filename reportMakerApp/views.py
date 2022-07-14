from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def logIn(req):
    if req.method == 'POST':
        # Get all data
        loginEmail = req.POST['email']
        loginPassword = req.POST['password']
        
        # Authentication
        user = authenticate(req, username=loginEmail.split('@')[0], password=loginPassword)

        if user != None:
            login(req, user)
            return redirect('home')
        else:
            messages.error(req, "Invalid Username or Password!")
            return redirect('login')
    elif req.method == 'GET':
        if req.user.is_authenticated:
            return redirect('home')
        else:
            return render(req, 'login.html')

def logOut(req):
    logout(req)
    messages.success(req, "Successfully logged out!")
    return redirect('login')
    
def signUp(req):
    if req.method == 'POST':
        # Get all data
        fname = req.POST['fname']
        lname = req.POST['lname']
        email = req.POST['email']
        password = req.POST['password']
        role = req.POST.get('role', 'leader')
        print(role)
        team = req.POST['team']
        
        # Create User
        user = User.objects.create_user(email.split('@')[0], email, password)
        user.first_name = fname
        user.last_name = lname
        user.role = role
        user.team = team
        user.save()

        messages.success(req, "Account Created Successfully!")
        return redirect('login')
    elif req.method == 'GET':
        context = {
            'roles':[
                ['leader', 'Team Leader'],
                ['member', 'Team Member']
            ]
        }
        return render(req, 'signup.html', context)
    
def test(req):
    return render(req, 'test.html')

def home(req):
    print(req.user.is_authenticated)
    if (req.user.is_authenticated == False):
        return redirect('login')
    else:
        context = {
            "teamName": "TeamName",
            "reporterName": "User Name",
            "reporterDesign":"Project Manager",
            "designation": "Graphic Designer",
            "lastReportTime": "1 hour ago",
            "ongoingWork": "Reports Page Design"
        }
        return render(req, "home.html", context)