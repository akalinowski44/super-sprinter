from django.urls import path

from . import views

app_name = 'sprinter'

urlpatterns = [
    path('', views.projects_list, name='projects_list'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('add/project/', views.add_project, name='add_project'),
    path('delete/project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('add/story/', views.add_story, name='add_story'),
    path('edit/project/<str:project_title>/', views.edit_project, name='edit_project'),
    path('edit/story/<int:story_id>/', views.edit_story, name='edit_story'),

]