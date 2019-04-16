from django.contrib import admin

from .models import Story, Project

admin.site.register(Project)
admin.site.register(Story)
