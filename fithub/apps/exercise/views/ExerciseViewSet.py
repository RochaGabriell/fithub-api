from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from fithub.apps.exercise.serializers import ExerciseSerializer
from fithub.apps.exercise.models import Exercise


class ExerciseViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os exercícios sejam visualizados ou editados. (GET, PUT, PATCH, DELETE)
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    filterset_fields = ['type_exercise',
                        'difficulty',
                        'muscles_primary',
                        'equipment'
                        ]
