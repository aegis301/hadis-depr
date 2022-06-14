from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "id",
            "title",
            "description",
            "created_at",
            "created_by",
            "dataforms",
            "visits",
            "type"
        )
