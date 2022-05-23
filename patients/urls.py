from django.urls import path
from . import views


urlpatterns = [
    ################################# Patients #################################
    path("", views.PatientListView.as_view(), name="patient-list"),
    path(
        "<int:pk_patient>/",
        views.PatientDetailView.as_view(),
        name="patient-detail",
    ),
    path("create/", views.PatientCreateView.as_view(), name="patient-create"),
    path(
        "<int:pk_patient>/update",
        views.PatientUpdateView.as_view(),
        name="patient-update",
    ),
    path(
        "<int:pk_patient>/delete/",
        views.PatientDeleteView.as_view(),
        name="patient-delete",
    ),
    ############################################# Visits
    path(
        "<int:pk_patient>/detail/visit/create",
        views.VisitCreateView.as_view(),
        name="visit-create",
    ),
    path(
        "<int:pk_patient>/detail/visit/delete",
        views.VisitDeleteView.as_view(),
        name="visit-delete",
    ),
    path(
        "<int:pk_patient>/detail/visit/<int:pk_visit>/detail",
        views.VisitDetailView.as_view(),
        name="visit-detail"
    ),
    ########################################################        Dataforms to Visits           #######################################
    path(
        "<int:pk_patient>/detail/visit/<int:pk_visit>/add_dataform",
        views.DataformAddView,
        name="dataform-add"
    ),
    
    
    
    path(
        "<int:pk_visit>/detail/create-instance",
        views.ItemInstanceCreateView,
        name="item-instance-create"
    )
]
