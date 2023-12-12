from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, permissions
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response

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
        if serializer.validated_data["default"] and Workout.objects.filter(user=serializer.validated_data["user"], default=True).exists():
            raise serializers.ValidationError(
                _("Já existe um treino padrão para este usuário."))
        serializer.save()

    def perform_update(self, serializer):
        if serializer.validated_data["default"] and Workout.objects.filter(user=serializer.validated_data["user"], default=True).exists():
            raise serializers.ValidationError(
                _("Já existe um treino padrão para este usuário."))
        serializer.save()

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAuthenticated, ]
        return super(WorkoutViewSet, self).get_permissions()

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user) | Workout.objects.filter(public=True)

    @action(detail=False, methods=['get'])
    def my(self, request):
        """
        Endpoint da API que permite que os treinos do usuário sejam visualizados. (GET)
        """
        queryset = Workout.objects.filter(user=request.user)
        serializer = WorkoutSerializer(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = WorkoutSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def default(self, request):
        """
        Endpoint da API que permite que o treino padrão seja visualizado. (GET)
        """
        workout = Workout.objects.filter(user=request.user, default=True)
        if workout.exists():
            serializer = WorkoutSerializer(workout[0])
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
