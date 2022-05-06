from django.urls import path
from . import views


urlpatterns = [
    path(
        "dataform/<int:pk>/detail/item/create",
        views.ItemCreateView,
        name="item-create",
    ),
    path(
        "dataform/<int:pk>/detail/item/delete",
        views.ItemDeleteView,
        name="item-delete",
    )
]
