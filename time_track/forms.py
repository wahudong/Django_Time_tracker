from django import forms
from .models import Project
from django.forms import ModelForm


class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ["projet_name", "completed", "operator"]