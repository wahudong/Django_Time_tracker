from django.shortcuts import render, redirect
from .models import Project, TimeList
from .forms import ProjectForm, CreateUserForm
from django.contrib import messages

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.urls import reverse
import json
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.

def home(request):
  if request.user.is_authenticated:
    mytest = 'Not a POST'
    hours = 0
    if request.method == 'POST':
      mytest = request.POST
      hours_unicode = request.body.decode('utf-8')
      # hours = json.load(hours_unicode)
      # hour = hours[0]



        # # form = ProjectForm(request.POST or None)
        # if form.is_valid():
        #   form.save()
        #   # user_projects = Project.objects.get(pk=1)
        #   messages.success(request,('The project has been created.'))
        #   return render(request, 'home.html', {'user': request.user})

    projects_of_user =  Project.objects.filter(operator = request.user)
    return render(request, 'home.html', {'hours':hours,'mytest':mytest,'user': request.user, 'projects_of_user':projects_of_user})

  else:
    return redirect('login')


def register(request):
  # if request.user.is_authenticated:
  #   return redirect('home')
  # else:
  form = CreateUserForm()
  if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Account was created for ' + user)
        return redirect('login')

  context={'form':form}
  return render(request, 'register.html', context)

# def loginPage(request):
#   context='I am in login 3'
#   return render(request,'login.html', {'context':context})

def loginPage(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password= password)

    if user is not None:
      login(request,user)
      return redirect('home')
    else:
      messages.info(request,'Username OR password is incorrect')

  context={}
  return render(request, 'login.html', context)

# def loginPage(request):
#   if request.user.is_authenticated:
#     return redirect('home')
#   else:
#     if request.method == 'POST':
#       username = request.POST.get('username')
#       password = request.POST.get('password')
#       user = authenticate(request, username=username, password= password)

#       if user is not None:
#         login(request,user)
#         return redirect('home')
#       else:
#         messages.info(request,'Username OR password is incorrect')

#     context={}
#     return render(request, 'login.html', context)


def logoutPage(request):
  logout(request)
  return redirect('login')



def create_project(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      form = ProjectForm(request.POST or None)
      if form.is_valid():
        form.save()
        projects_of_user =  Project.objects.filter(operator = request.user)
        messages.success(request,('The project has been created.'))
        # request.method == ''
        return redirect('home')
    else:
      # user_projects = Project.objects.get(pk=1)

      return render(request, 'create_project.html', {'user': request.user})
  else:
    return redirect('login')



def me(request):
  context='Ben, hello'
  return render(request,'me.html', {'context':context})
