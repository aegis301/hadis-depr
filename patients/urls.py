from django.urls import path
from . import views


urlpatterns = [
    ################################# Patients #################################
    path("", views.PatientListView.as_view(), name="patient-list"),
    path(
        "<int:pk>/",
        views.PatientDetailView.as_view(),
        name="patient-detail",
    ),
    path("create/", views.PatientCreateView.as_view(), name="patient-create"),
    path(
        "<int:pk>/update",
        views.PatientUpdateView.as_view(),
        name="patient-update",
    ),
    path(
        "<int:pk>/delete/",
        views.PatientDeleteView.as_view(),
        name="patient-delete",
    ),
    ############################################# Visits
    path(
        "<int:pk>/detail/visit/create",
        views.VisitCreateView.as_view(),
        name="visit-create",
    ),
    path(
        "<int:pk>/detail/visit/delete",
        views.VisitDeleteView.as_view(),
        name="visit-delete",
    )
]
