from rest_framework import viewsets, permissions

from fithub.apps.manager.serializers import DayExerciseSerializer
from fithub.apps.manager.models import DayExercise


class DayExerciseViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API para listar e criar exercícios de um dia de treino. (GET, POST, PUT, DELETE)
    """
    queryset = DayExercise.objects.all()
    serializer_class = DayExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
