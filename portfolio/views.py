from django.shortcuts import render
from .models import Project
from django.shortcuts import render, get_object_or_404

# Create your views here


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})


def project_detail(request, project_id):
    project= get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/portfolio_detail.html', {'project':project})
