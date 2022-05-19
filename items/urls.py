from django.urls import path
from . import views


urlpatterns = [
    path(
        "/create",
        views.ItemCreateView,
        name="item-create"
    ),
    path(
        "<int:pk_item>/delete",
        views.ItemDeleteView,
        name="item-delete"
    ),
    path(
        "<int:pk_item>/update",
        views.ItemUpdateView,
        name="item-update"
    ),
    path("",
         views.ItemListView.as_view(),
         name="item-list"),
    path("<int:pk_item>/detail",
         views.ItemDetailView.as_view(),
         name="item-detail"),
    path(
        "create-instance",
        views.ItemInstanceCreateView,
        name="item-instance-create"
    )
]
