from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Team)
admin.site.register(Member)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'joined_at')
    search_fields = ('name', 'email', 'role')
    list_filter = ('joined_at', 'team')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'team', 'start_date', 'end_date', 'status')
    search_fields = ('title', 'description', 'status')
    list_filter = ('team', 'status', 'start_date', 'end_date')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'assigned_to', 'priority', 'progress', 'start_date', 'end_date')
    search_fields = ('title', 'description', 'milestone')
    list_filter = ('priority', 'project', 'assigned_to', 'start_date', 'end_date')

admin.site.unregister(Team)
admin.site.unregister(Member)
admin.site.unregister(Project)
admin.site.unregister(Task)

admin.site.register(Team, TeamAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)