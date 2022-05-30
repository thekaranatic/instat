from django.contrib import admin

# Register the models 

from .models import Phase, Project

admin.site.register(Project)
admin.site.register(Phase)
