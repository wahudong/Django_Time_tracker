from django.shortcuts import render, redirect
from .models import Project, TimeList
from .forms import ProjectForm, CreateUserForm
from django.contrib import messages

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

def register(request):
  if request.user.is_authenticated:
    return redirect('home')
  else:
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
      # return redirect('home')
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

def me(request):
  context='Ben, hello'
  return render(request,'me.html', {'context':context})
