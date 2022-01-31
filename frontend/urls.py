from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hadis-home'),
    path('forms/', views.forms, name='forms-show'),
    path('show_patients/', views.show_page, name='patients-show')
]
