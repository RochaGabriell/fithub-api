from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, permissions
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from fithub.apps.manager.serializers import WorkoutSerializer
from fithub.apps.manager.models import Workout


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os treinos sejam visualizados ou editados. (GET, PUT, PATCH, DELETE)
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    filterset_fields = ['difficulty', 'public']

    def perform_create(self, serializer):
        if serializer.validated_data["is_default"] and Workout.objects.filter(user=serializer.validated_data["user"], is_default=True).exists():
            raise serializers.ValidationError(
                _("Já existe um treino padrão para este usuário."))
        serializer.save()

    def perform_update(self, serializer):
        if serializer.validated_data["is_default"] and Workout.objects.filter(user=serializer.validated_data["user"], is_default=True).exists():
            raise serializers.ValidationError(
                _("Já existe um treino padrão para este usuário."))
        serializer.save()

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user) | Workout.objects.filter(public=True)
