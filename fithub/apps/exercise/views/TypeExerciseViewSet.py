from rest_framework import viewsets, permissions

from fithub.apps.exercise.serializers import TypeExerciseSerializer
from fithub.apps.exercise.models import TypeExercise


class TypeExerciseViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os tipos de exercício sejam visualizados ou editados. (GET, PUT, PATCH, DELETE)
    """
    queryset = TypeExercise.objects.all()
    serializer_class = TypeExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
