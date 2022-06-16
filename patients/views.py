from django.contrib.auth.mixins import LoginRequiredMixin
from patients.models import Patient
from django.shortcuts import render

from .serializers import PatientSerializer
from rest_framework import generics


class PatientView(LoginRequiredMixin, generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

def test(request):
    return render(request, 'patients/test.html')