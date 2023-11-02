from rest_framework import viewsets, permissions

from fithub.apps.manager.serializers import WorkoutDaySerializer
from fithub.apps.manager.models import WorkoutDay


class WorkoutDayViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os dias de treino sejam visualizados ou editados. (GET, PUT, PATCH, DELETE)
    """
    queryset = WorkoutDay.objects.all()
    serializer_class = WorkoutDaySerializer
    permission_classes = [permissions.IsAuthenticated]
