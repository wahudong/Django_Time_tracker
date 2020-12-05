from django.shortcuts import render, redirect


# Create your views here.

def home(request):
  context1= 'hello, '
  context2='ben'
  return render(request, 'home.html', {'context1': context1, 'context2':context2} )