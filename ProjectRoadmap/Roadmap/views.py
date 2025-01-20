from django.shortcuts import render
from .models import Team
# Create your views here.
def index(request):
    teams = Team.objects.all()
    context = {
        'teams': teams,
    }
    return render(request, 'index.html', context)

def roadmap(request):
    return render(request, 'roadmap.html')

def about(request):
    return render(request, 'about.html')

def task(request):
    tasks = [
        {'title': 'Task 1', 'description': 'Description for task 1', 'status': 'pending'},
        {'title': 'Task 2', 'description': 'Description for task 2', 'status': 'completed'},
        {'title': 'Task 3', 'description': 'Description for task 3', 'status': 'in-progress'}
    ]
    context = {'tasks': tasks}
    return render(request, 'task.html', context)