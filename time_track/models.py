from django.db import models

# Create your models here.

class Project(models.Model):
  projet_name = models.CharField(max_length=200)
  completed = models.BooleanField(default = False)

# class TimeList(models.Model):
#   start_time =  models.DateTimeField(auto_now=False)
#   end_time = models.DateTimeField(auto_now=False)
#   time_length = models.DecimalField(max_digits=None, decimal_places=None)

#   def __str__(self):
#     return str(self.start_time) + '|' + str(self.end_time) + str(self.decimal_places)
