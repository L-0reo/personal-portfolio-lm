from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})


def tictactoe(request):
    return render(request, 'portfolio/tictactoe.html')
