from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

# Create your models here.
class TeamCode(models.Model):
    user_created = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user")
    postCode = models.CharField(max_length=8, unique=True)
    postName = models.CharField(max_length=50, unique=True)
    class Meta:
        ordering = ['postCode']
    def __str__(self):
        return f"{self.postName} - {self.postCode}"


class Report(models.Model):
    report_title = models.CharField(max_length=100)
    report_desc = models.TextField()
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_code = models.ForeignKey(TeamCode, on_delete=models.RESTRICT)
    created = models.DateTimeField(default=datetime.now)
    class Meta:
        ordering = ['-created']
    
    def get_by_team_name(team_name, query):
        # query = Report.objects.all()
        reportsData = []
        for n, i in enumerate(query):
            teamName = query[n].reporter.get_team_name()
            if teamName == team_name:
                reportsData.append((query[n]))
            if len(reportsData) == 100:
                break
        return reportsData

    def __str__(self) -> str:
        return f"{self.report_title} - {self.reporter}"

class Profile(models.Model):
    """
    Fields:
    user: User from the created user
    user_id: Unique User Id
    phone_number: Mobile number of the user
    gender
    dob
    college_id 
    teamName
    teamCode
    """
    gender = (
        ('n', 'Not Specified'),
        ('m', 'Male'),
        ('f', 'Female'),
        ('t', 'Trans'),
    )

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(choices=gender, max_length=1, default='n')
    Date_of_Birth = models.DateField(default=datetime(2000, 1, 1))
    phone_number = models.CharField(max_length=10, default="None")
    college_id = models.CharField(max_length=7, default="None")
    teamCodes = models.ManyToManyField(TeamCode)
    is_verified = models.BooleanField(default=False)
    auth_token = models.CharField(max_length=100)
    class Meta:
        abstract = True

class Leader(Profile):
    team_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        try:
            return f"{self.user.first_name} {self.user.last_name} - {self.team_name}"
        except:
            return super().__str__()
    def save(self, *args, **kwargs) -> None:
        if Member.objects.filter(user=self.user).first() == None:
            return super().save(*args, **kwargs)
        else:
            raise ValidationError(f"{self.user.username} is already a member, migrate it to make it a leader.")
            

class Member(Profile):
    leader = models.ForeignKey(Leader, on_delete=models.RESTRICT)
    def __str__(self) -> str:
        try:
            return f"{self.user.first_name} {self.user.last_name} - {self.team_name}"
        except:
            return super().__str__()
    def save(self, *args, **kwargs) -> None:
        if Leader.objects.filter(user=self.user).first() == None:
            return super().save(*args, **kwargs)
        else:
            raise ValidationError(f"{self.user.username} is already a leader, migrate it to make it a member.")

# User Functions
def get_name(self):
    return f'{self.first_name} {self.last_name} - {self.username}'

def get_team_name(self):
    try:
        if self.member.leader.team_name != None:
            return self.member.leader.team_name
    except:pass
    try:
        if self.leader.team_name != None:
            return self.leader.team_name
    except:pass
    else:
        return None

def get_leader_user(self):
    try:
        if self.member.leader.user != None:
            return self.member.leader.user
    except:pass
    try:
        if self.leader.user != None:
            return self.leader.user
    except:pass
    return None

def get_teamCodes(self):
    try:
        if self.member.teamCodes != None:
            return self.member.teamCodes
    except:pass
    try:
        if self.leader.teamCodes != None:
            return self.leader.teamCodes
    except:pass
    return None

User.add_to_class("__str__", get_name)
User.add_to_class("get_team_name", get_team_name)
User.add_to_class("get_leader_user", get_leader_user)
User.add_to_class("get_teamCodes", get_teamCodes)
