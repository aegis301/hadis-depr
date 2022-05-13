from django.urls import path
from . import views


urlpatterns = [
    path(
        "dataform/<int:pk_df>/detail/item/create",
        views.ItemCreateView,
        name="item-create"
    ),
    path(
        "dataform/<int:pk_df>/detail/item/<int:pk_item>/delete",
        views.ItemDeleteView,
        name="item-delete"
    ),
    path(
        "dataform/<int:pk_df>/detail/item/<int:pk_item>/update",
        views.ItemUpdateView,
        name="item-update"
    ),
    path("item/",
         views.ItemListView.as_view(),
         name="item-list")
]
