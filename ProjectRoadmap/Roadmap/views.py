from django.shortcuts import render
from .models import Team, Project, Member, Task
# Create your views here.
def index(request):
    teams = Team.objects.all()
    members = Member.objects.all()
    projects = Project.objects.all()
    tasks = Task.objects.all()
    context = {
        'teams': teams,
        'members': members,
        'projects': projects,
        'tasks': tasks
    }
    return render(request, 'index.html', context)

def roadmap(request):
    return render(request, 'roadmap.html')

def about(request):
    return render(request, 'about.html')

def taskinfo(request):
    tasks = Task.objects.all()
    projects = Project.objects.all()

    context = {
        'tasks': tasks,
        'projects': projects
    }
    return render(request, 'task.html', context)

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    tasks = Task.objects.filter(project=project)
    context = {
        'project': project,
        'tasks': tasks
    }
    return render(request, 'project_detail.html', context)