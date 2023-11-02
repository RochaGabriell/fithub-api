from rest_framework import viewsets, permissions

from fithub.apps.manager.serializers import WorkoutSerializer
from fithub.apps.manager.models import Workout


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os treinos sejam visualizados ou editados. (GET, PUT, PATCH, DELETE)
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]
