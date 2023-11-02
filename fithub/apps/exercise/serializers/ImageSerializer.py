from rest_framework import serializers

from fithub.apps.exercise.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
