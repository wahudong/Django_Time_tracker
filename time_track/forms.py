from django import forms
from .models import Project
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ["projet_name", "completed", "operator"]



class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username','email','password1','password2']