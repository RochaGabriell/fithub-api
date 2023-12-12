from django_filters.rest_framework import DjangoFilterBackend
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['workout']

    def perform_create(self, serializer):
        if WorkoutDay.objects.filter(workout=serializer.validated_data["workout"], day=serializer.validated_data["day"]).exists():
            raise serializers.ValidationError(
                _("Já existe um treino para este dia da semana."))
        serializer.save()

    def perform_update(self, serializer):
        instance = self.get_object()

        if "day" in serializer.validated_data and instance.day != serializer.validated_data["day"]:
            workout = serializer.validated_data["workout"]
            day = serializer.validated_data["day"]

            if WorkoutDay.objects.filter(workout=workout, day=day).exists():
                raise serializers.ValidationError(
                    _("Já existe um treino para este dia da semana.")
                )

        serializer.save()

    def get_queryset(self):
        return WorkoutDay.objects.filter(workout__user=self.request.user)
