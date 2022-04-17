from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    ################################# DataForms #################################
    # path("forms/", views.forms, name="forms-show"),
    path(
        "list/", views.DataFormListView.as_view(), name="dataform-list"
    ),
    path(
        "<int:pk>/detail",
        views.DataFormDetailView.as_view(),
        name="dataform-detail",
    ),
    path(
        "<int:pk>/delete/",
        views.DataFormDeleteView.as_view(),
        name="dataform-delete",
    ),
    path(
        "create/",
        views.DataFormCreateView.as_view(),
        name="dataform-create",
    ),
    path(
        "<int:pk>/update",
        views.DataFormUpdateView.as_view(),
        name="dataform-update",
    ),
    ################################# Items #################################
    
]
