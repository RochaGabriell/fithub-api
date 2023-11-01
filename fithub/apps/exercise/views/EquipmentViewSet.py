from rest_framework import viewsets, permissions

from fithub.apps.exercise.serializers import EquipmentSerializer
from fithub.apps.exercise.models import Equipment


class EquipmentViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os equipamentos sejam visualizados ou editados. (GET, PUT, PATCH, DELETE)
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]
