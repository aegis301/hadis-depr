from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='hadis-home'),
    path('forms/', views.forms, name='forms-show'),
    path('show_patients/', views.show_page, name='patients-show'),
    path('user_registration/', views.register_user, name='user-registration'),
    path('user_login/', auth_views.LoginView.as_view(template_name='frontend/user_login.html'), name="user-login"),
    path('user_logout/', auth_views.LogoutView.as_view(template_name='frontend/user_logout.html'), name="user-logout"),
    path('user_profile/', views.user_profile, name="user-profile")
]
