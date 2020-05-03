from django.contrib import admin

# Register your models here.
from projects.models import Project

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
