from rest_framework import viewsets, permissions

from fithub.apps.exercise.serializers import ImageSerializer
from fithub.apps.exercise.models import Image


class ImageViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que as imagens sejam visualizadas ou editadas. (GET, PUT, PATCH, DELETE)
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]
