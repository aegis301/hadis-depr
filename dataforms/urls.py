from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    ################################# DataForms #################################
    # path("forms/", views.forms, name="forms-show"),
    path(
        "list/", views.DataFormTemplateListView.as_view(), name="dataform-list"
    ),
    path(
        "<int:pk>/detail",
        views.DataFormTemplateDetailView.as_view(),
        name="dataform-detail",
    ),
    path(
        "<int:pk>/delete/",
        views.DataFormTemplateDeleteView.as_view(),
        name="dataform-delete",
    ),
    path(
        "create/",
        views.DataFormTemplateCreateView.as_view(),
        name="dataform-create",
    ),
    path(
        "<int:pk>/update",
        views.DataFormTemplateUpdateView.as_view(),
        name="dataform-update",
    ),
    ################################# Items #################################
    path(
        "<int:pk>/item/create",
        views.ItemCreateView.as_view(),
        name="item-create",
    ),
]
