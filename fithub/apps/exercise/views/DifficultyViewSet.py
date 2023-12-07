from rest_framework import viewsets, permissions

from fithub.apps.exercise.serializers import DifficultySerializer
from fithub.apps.exercise.models import Difficulty


class DifficultyViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que as dificuldades sejam visualizadas ou editadas. (GET, PUT, PATCH, DELETE)
    """
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
