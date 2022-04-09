from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
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
    )
]
