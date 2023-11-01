from rest_framework import viewsets, permissions

from fithub.apps.exercise.serializers import ExerciseSerializer
from fithub.apps.exercise.models import Exercise


class ExerciseViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os exercícios sejam visualizados ou editados. (GET, PUT, PATCH, DELETE)
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]
