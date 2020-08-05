from django.shortcuts import render
from projects.models import Project

# Create your views here.


def project_index(request):
    projects = Project.objects.all()
    for project in projects:
        if len(project.description) > 100:
            project.description = project.description[:100] + '...'
    context = {"projects": projects}
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}

    return render(request, "project_detail.html", context)
