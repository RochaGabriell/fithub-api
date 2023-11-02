from rest_framework import viewsets, permissions

from fithub.apps.account.serializers import MeasurementsSerializer
from fithub.apps.account.models import Measurements


class MeasurementsViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que as medidas sejam visualizadas ou editadas. (GET, PUT, PATCH, DELETE)
    """
    queryset = Measurements.objects.all()
    serializer_class = MeasurementsSerializer
    permission_classes = [permissions.IsAuthenticated]
