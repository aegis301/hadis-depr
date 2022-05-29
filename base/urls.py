from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="hadis-home"),
    path("javascript", views.javascript, name="hadis-js"),
]
