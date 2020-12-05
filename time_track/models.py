from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
  projet_name = models.CharField(max_length=200)
  completed = models.BooleanField(default = False)
  operator = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
        return "%s | %s" % (self.projet_name, self.operator.username)

# class TimeList(models.Model):
#   start_time =  models.DateTimeField(auto_now=False)
#   end_time = models.DateTimeField(auto_now=False)
#   time_length = models.DecimalField(max_digits=None, decimal_places=None)

#   def __str__(self):
#     return str(self.start_time) + '|' + str(self.end_time) + str(self.decimal_places)
