from django.urls import path
from . import views

app_name = 'Roadmap'

urlpatterns = [
    path('', views.index, name='index'),
    # path('create/', views.create_roadmap, name='create_roadmap'),
    # path('detail/<int:roadmap_id>/', views.roadmap_detail, name='roadmap_detail'),
    # path('edit/<int:roadmap_id>/', views.edit_roadmap, name='edit_roadmap'),
    # path('delete/<int:roadmap_id>/', views.delete_roadmap, name='delete_roadmap'),
    path('about/', views.about, name='about'),
    path('roadmap/', views.roadmap, name='roadmap'),
    path('task/', views.task, name='task'),
]