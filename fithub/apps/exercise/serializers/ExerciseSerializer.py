from rest_framework import serializers

from fithub.apps.exercise.models import Exercise
from .ImageSerializer import ImageSerializer


class ExerciseSerializer(serializers.ModelSerializer):

    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Exercise
        fields = [
            'id',
            'name',
            'type_exercise',
            'difficulty',
            'instructions',
            'muscles_primary',
            'muscles_secondary',
            'equipment',
            'variations',
            'weight_unit',
            'images'
        ]
