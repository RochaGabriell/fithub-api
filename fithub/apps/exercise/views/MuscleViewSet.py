from rest_framework import viewsets, permissions

from fithub.apps.exercise.serializers import MuscleSerializer
from fithub.apps.exercise.models import Muscle


class MuscleViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os músculos sejam visualizados ou editados. (GET, PUT, PATCH, DELETE)
    """
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
    permission_classes = [permissions.IsAuthenticated]
