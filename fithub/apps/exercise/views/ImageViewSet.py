from rest_framework import viewsets, permissions
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from fithub.apps.exercise.serializers import ImageSerializer
from fithub.apps.exercise.models import Image


class ImageViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que as imagens sejam visualizadas ou editadas. (GET, PUT, PATCH, DELETE)
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.validated_data["is_main"] and Image.objects.filter(exercise=serializer.validated_data["exercise"], is_main=True).exists():
            raise serializers.ValidationError(
                _("Já existe uma imagem principal para este exercício."))
        serializer.save()

    def perform_update(self, serializer):
        if serializer.validated_data["is_main"] and Image.objects.filter(exercise=serializer.validated_data["exercise"], is_main=True).exists():
            raise serializers.ValidationError(
                _("Já existe uma imagem principal para este exercício."))
        serializer.save()