from django.shortcuts import render, redirect
from .models import Project, TimeList
from .forms import ProjectForm
from django.contrib import messages



# Create your views here.

def home(request):
  if request.method == 'POST':
    form = ProjectForm(request.POST or None)
    if form.is_valid():
      form.save()
      user_projects = Project.objects.get(pk=1)
      messages.success(request,('The project has been created.'))
      return render(request, 'home.html', {'user_projects': user_projects})
  else:
    user_projects = Project.objects.all
    return render(request, 'home.html', {'user_projects': user_projects})
