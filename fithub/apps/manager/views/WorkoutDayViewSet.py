from rest_framework import viewsets, permissions
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from fithub.apps.manager.serializers import WorkoutDaySerializer
from fithub.apps.manager.models import WorkoutDay


class WorkoutDayViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os dias de treino sejam visualizados ou editados. (GET, PUT, PATCH, DELETE)
    """
    queryset = WorkoutDay.objects.all()
    serializer_class = WorkoutDaySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def perform_create(self, serializer):
        if WorkoutDay.objects.filter(workout=serializer.validated_data["workout"], day=serializer.validated_data["day"]).exists():
            raise serializers.ValidationError(
                _("Já existe um treino para este dia da semana."))
        serializer.save()

    def perform_update(self, serializer):
        if WorkoutDay.objects.filter(workout=serializer.validated_data["workout"], day=serializer.validated_data["day"]).exists():
            raise serializers.ValidationError(
                _("Já existe um treino para este dia da semana."))
        serializer.save()
