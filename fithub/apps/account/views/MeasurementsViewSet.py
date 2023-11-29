from rest_framework import viewsets, permissions
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from fithub.apps.account.serializers import MeasurementsSerializer
from fithub.apps.account.models import Measurements


class MeasurementsViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que as medidas sejam visualizadas ou editadas. (GET, PUT, PATCH, DELETE)
    """
    queryset = Measurements.objects.all()
    serializer_class = MeasurementsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if Measurements.objects.filter(user=serializer.validated_data["user"]).exists():
            last_measure = Measurements.objects.filter(
                user=serializer.validated_data["user"]).order_by('-date')[0]
            if last_measure.date.month == serializer.validated_data["date"].month and last_measure.date.year == serializer.validated_data["date"].year:
                raise serializers.ValidationError(
                    _("Já existe uma medida para este mês."))
        serializer.save()
