from django.urls import path
from . import views

app_name = 'Roadmap'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('roadmap/', views.roadmap, name='roadmap'),
    path('task/', views.taskinfo, name='task'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]
