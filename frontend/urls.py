from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="hadis-home"),
    ################################# Patients #################################
    path("patient/list/", views.PatientListView.as_view(), name="patient-list"),
    path(
        "patient/<int:pk>/",
        views.PatientDetailView.as_view(),
        name="patient-detail",
    ),
    path("patient/create/", views.PatientCreateView.as_view(), name="patient-create"),
    path(
        "patient/<int:pk>/update",
        views.PatientUpdateView.as_view(),
        name="patient-update",
    ),
    path(
        "patient/<int:pk>/delete/",
        views.PatientDeleteView.as_view(),
        name="patient-delete",
    ),
    
    ################################# Users #################################
    path("user_registration/", views.register_user, name="user-registration"),
    path(
        "user_login/",
        auth_views.LoginView.as_view(template_name="frontend/user_login.html"),
        name="user-login",
    ),
    path(
        "user_logout/",
        auth_views.LogoutView.as_view(template_name="frontend/user_logout.html"),
        name="user-logout",
    ),
    path("user_profile/", views.user_profile, name="user-profile"),
    path("user_list/<str:username>/", views.UserPatientListView.as_view(), name="user-posts"),
    
    ################################# DataForms #################################
    # path("forms/", views.forms, name="forms-show"),
    path("dataform/list/", views.DataFormListView.as_view(), name="dataform-list"),
    path("dataform/<int:pk>/detail", views.DataFormDetailView.as_view(), name="dataform-detail"),
    path("dataform/<int:pk>/delete/", views.DataFormDeleteView.as_view(), name="dataform-delete")
]
