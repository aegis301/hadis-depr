from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    ################################# DataForms #################################
    # path("forms/", views.forms, name="forms-show"),
    path(
        "dataform/list/", views.DataFormTemplateListView.as_view(), name="dataform-list"
    ),
    path(
        "dataform/<int:pk>/detail",
        views.DataFormTemplateDetailView.as_view(),
        name="dataform-detail",
    ),
    path(
        "dataform/<int:pk>/delete/",
        views.DataFormTemplateDeleteView.as_view(),
        name="dataform-delete",
    ),
    path(
        "dataform/create/",
        views.DataFormTemplateCreateView.as_view(),
        name="dataform-create",
    ),
    path(
        "dataform/<int:pk>/update",
        views.DataFormTemplateUpdateView.as_view(),
        name="dataform-update",
    ),
    ################################# Items #################################
    path(
        "dataform/<int:pk>/item/create",
        views.ItemCreateView.as_view(),
        name="item-create",
    ),
]
