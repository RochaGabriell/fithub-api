from rest_framework import viewsets, permissions

from fithub.apps.exercise.serializers import WeightUnitSerializer
from fithub.apps.exercise.models import WeightUnit


class WeightUnitViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que as unidades de peso sejam visualizadas ou editadas. (GET, PUT, PATCH, DELETE)
    """
    queryset = WeightUnit.objects.all()
    serializer_class = WeightUnitSerializer
    permission_classes = [permissions.IsAuthenticated]
