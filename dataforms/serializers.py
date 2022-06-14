from rest_framework import serializers
from .models import DataForm


class DataFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataForm
        fields = ("id", "title", "description", "created_at", "created_by")
