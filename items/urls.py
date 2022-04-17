from django.urls import path
from . import views


urlpatterns = [
    path(
        "<int:pk>/item/create",
        views.ItemCreateView.as_view(),
        name="item-create",
    )
]
