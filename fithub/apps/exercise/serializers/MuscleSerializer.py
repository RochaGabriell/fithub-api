from rest_framework import serializers

from fithub.apps.exercise.models import Muscle


class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = "__all__"