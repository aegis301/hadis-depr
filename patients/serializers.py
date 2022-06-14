from rest_framework import serializers
from .models import Patient, Visit


class PatientSerializer(serializers.Serializer):
    class Meta:
        model = Patient
        fields = (
            "id",
            "last_name",
            "first_name",
            "date_of_birth",
            "kis_id",
            "gender",
            "created_at",
            "created_by",
            "main_diagnosis",
        )

class VisitSerializer(serializers.Serializer):
    class Meta:
        model = Visit
        fields = (
            "patient",
            "visit_date",
            "created_by",
            "patient_in_hospital"
        )