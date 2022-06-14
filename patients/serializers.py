from rest_framework import serializers


class PatientSerializer(serializers.Serializer):
    class Meta:
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
