from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Leader, Member, Report, TeamCode

# Clear Recent Actions Log
# from django.contrib.admin.models import LogEntry
# LogEntry.objects.all().delete()

# Utilities
def log(message):
    with open("error.log", "a") as f:
        f.write(str(message) + "\n")

def getReportsData(req):
    team_name = req.user.get_team_name()
    return Report.get_by_team_name(team_name, Report.objects.all())

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
            messages.success(req, "You are already logged in!")
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
        fname = req.POST['fname'].replace(" ", "").lower().capitalize()
        lname = req.POST['lname'].replace(" ", "").lower().capitalize()
        email = req.POST['email'].replace(" ", "").lower()
        password = req.POST['password']
        role = req.POST.get('role')
        team = req.POST['team']
        
        # Check User
        if (User.objects.filter(username=email.split('@')[0]).first() != None):
            messages.error(req, "User already exists!")
            return redirect('login')

        # Create User
        user = User.objects.create_user(email.split('@')[0], email, password)
        user.first_name = fname
        user.last_name = lname

        user.save()

        if role == "member":
            member = Member.objects.create(user=user)
            teamCodes = team.capitalize().replace("O", "0").replace(" ", "").split(",")
            for i in teamCodes:
                member.teamCodes.add(TeamCode.objects.get(postCode=i))
            
            member.leader.add(Leader.objects.get(user=TeamCode.objects.get(postCode=teamCodes[0]).user_created))
            member.save()
        elif role == "leader":
            member = Leader.objects.create(user=user)
            member.team = team
            member.save()

        messages.success(req, "Account Created Successfully!")
        return redirect('login')
    elif req.method == 'GET':
        if req.user.is_authenticated:
            messages.success(req, "You are already registered!")
            return redirect('home')
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
    if (req.user.is_authenticated == False):
        return redirect('login')
    else:
        posts = TeamCode.objects.filter(user_created=req.user.get_leader_user()).values_list('postCode', 'postName', 'id')
        result = []
        for m, i in enumerate(posts):
            result.append(list(i))
            i = list(i)
            try:
                data = Report.objects.filter(post_code=result[m][2]).values_list('report_title', 'created')

                if len(data) != 0:
                    i.extend(data[0])
                    i[4] = i[4].strftime("%I:%M%p").lower()

            except Exception as e:
                log(e)
            result[m] = i

        
        context = {
            "home":"on",
            "posts":result,
            "reportsData":getReportsData(req)
        }
        return render(req, "home.html", context)

def srijan(req):
    return HttpResponse("Srijan")

def reports(req):
    if (req.user.is_authenticated == False):
        return redirect('login')
    if req.method == "GET":
        context = {
            "reports":"on",
        }
        
        try:
            post = req.GET['post'].upper()
            team_name = req.user.get_team_name()
            if req.user.get_leader_user() != TeamCode.objects.get(postCode=post).user_created:
                context["reportsData"] = getReportsData(req)
                context["postCodes"] = list(req.user.get_teamCodes().values_list('postCode', 'postName'))
                print("a")
            else:
                context["reportsData"] = Report.get_by_team_name(team_name, Report.objects.filter(post_code=TeamCode.objects.get(postCode=post)))
                posts = []
                for i in list(req.user.get_teamCodes().values_list('postCode', 'postName')):
                    if i[0] == post:
                        i = list(i)
                        i.append('selected')
                    posts.append(i)
                context["postCodes"] = posts
        except Exception as e:
            log(e)
            print("Exception")
            context["reportsData"] = getReportsData(req)
            context["postCodes"] = list(req.user.get_teamCodes().values_list('postCode', 'postName'))
        return render(req, "reports.html", context=context)

def settings(req):
    if (req.user.is_authenticated == False):
        return redirect('login')
    if req.method == "GET":
        context = {
            "settings":"on",
            "reportsData":getReportsData(req)
        }
        return render(req, "settings.html", context=context)

def profile(req):
    if (req.user.is_authenticated == False):
        return redirect('login')
    if req.method == "GET":
        context = {
            "reportsData":getReportsData(req)
        }
        return render(req, "profile.html", context=context)

def report(req):
    if (req.user.is_authenticated == False):
        return redirect('login')
    if req.method == "GET":
        reportId = req.GET.get('id')
        try:
            reportData = Report.objects.get(id=reportId)
        except:
            return redirect('reports')
        if reportData.reporter.get_leader_user() != req.user.get_leader_user():
            return redirect('reports')
        context = {
            "reportsData":getReportsData(req),
            "reportData":reportData,
        }
        return render(req, "report.html", context=context)

def forgotPass(req):
    return HttpResponse("Fogot Password, Go to hell!!!")

def errorPage(req):
    print(req.message)
    return HttpResponse("{{for message in messages}}")

def addReport(req):
    title = req.POST['title']
    desc = req.POST['desc']
    postCode = req.POST['postCode']
    postCode = TeamCode.objects.get(postCode=postCode)

    report = Report(report_title=title, report_desc=desc, reporter=req.user, post_code=postCode)
    report.save()
    return redirect('reports')

# Error handling
# def handler404(request, exception):
#     return render(request, "400.html", context=exception)


# def handler500(request, template_name="500.html"):
#     print(request, template_name)
#     print("Hello")
#     print(RequestContext(request))
#     return render(request, template_name)