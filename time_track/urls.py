from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  # path('home/<list_id>', views.home, name='home'),
  path('register/', views.register, name='register'),
  path('login/', views.loginPage, name="login"),
  path('me/', views.me, name='me'),
  # path('logout/', views.logoutUser, name="logout"),
  path('logout/', views.logoutPage, name="logout"),
]