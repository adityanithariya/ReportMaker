from django.contrib import admin
from .models import Leader, Member, TeamCode, Report
from django.contrib.auth.models import User

# class UserAdmin(admin.ModelAdmin):
    # list_display = ['username', 'email', ]

class TeamCodeAdmin(admin.ModelAdmin):
    list_display = ['postCode', 'postName', 'user_created', 'id']

class LeaderAdmin(admin.ModelAdmin):
    list_display = ['user', 'team_name', 'college_id', 'id']

class MemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'leader', 'college_id', 'id']

class ReportAdmin(admin.ModelAdmin):
    list_display = ['report_title', 'reporter', 'post_code', 'created', 'id']

# Register your models here.
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

admin.site.register(Leader, LeaderAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(TeamCode, TeamCodeAdmin)