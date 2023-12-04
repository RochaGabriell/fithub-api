from rest_framework import viewsets, permissions, serializers
from django.utils.translation import gettext_lazy as _
from datetime import datetime

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
        if Measurements.objects.filter(
                user=serializer.validated_data["user"]).exists():

            last_measure = Measurements.objects.filter(
                user=serializer.validated_data["user"]).order_by('-created_at').first()

            date_now = datetime.now().month

            if last_measure.created_at.month == date_now:
                raise serializers.ValidationError(
                    {"detail": _("Você já cadastrou suas medidas esse mês.")})

        serializer.save()

    def get_queryset(self):
        return Measurements.objects.filter(user=self.request.user)


class MeasurementsListByUser(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Endpoint da API que permite que as medidas do usuário logado sejam visualizadas. (GET)
    """
    queryset = Measurements.objects.all()
    serializer_class = MeasurementsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Measurements.objects.filter(user=self.request.user).order_by('-created_at')
