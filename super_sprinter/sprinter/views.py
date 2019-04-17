from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Project, Story


def projects_list(request):
    projects_list = Project.objects.all()
    context = {'projects_list': projects_list}
    return render(request, 'sprinter/projects_list.html', context)

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    stories = Story.objects.filter(project = project_id)
    context = {'project': project,
               'stories': stories}
    return render(request, 'sprinter/project_details.html', context)

def add_project(request):
    project_title = request.POST['project_title']
    proj = Project(project_title=project_title)
    proj.save()
    return redirect('sprinter:projects_list')

def delete_project(request, project_id):
    proj = Project.objects.get(id=project_id)
    proj.delete()
    return redirect('sprinter:projects_list')

def add_story(request):
    return HttpResponse("You can add new user's story here.")

def edit_story(request, story_id):
    return HttpResponse("You are editing story number %s now." % story_id)

def edit_project(request, project_title):
    return HttpResponse("You are editing project %s" % project_title)
