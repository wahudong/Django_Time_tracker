from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
  projet_name = models.CharField(max_length=200)
  completed = models.BooleanField(default = False)
  operator = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
        return self.projet_name + self.operator.username

class TimeList(models.Model):
  start_time =  models.DateTimeField(auto_now=False)
  end_time = models.DateTimeField(auto_now=False)
  time_length = models.DecimalField(max_digits=7, decimal_places=2)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.start_time) + ' | ' + str(self.end_time) +' | '+ str(self.time_length)
