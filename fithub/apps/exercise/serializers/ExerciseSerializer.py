from rest_framework import serializers

from fithub.apps.exercise.models import Exercise
from .ImageSerializer import ImageSerializer


class ExerciseSerializer(serializers.ModelSerializer):

    muscles_primary = serializers.SerializerMethodField()
    muscles_secondary = serializers.SerializerMethodField()
    equipment = serializers.SerializerMethodField()
    variations = serializers.SerializerMethodField()
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

    def get_muscles_primary(self, obj):
        return obj.muscles_primary.values('id', 'name', 'is_front')

    def get_muscles_secondary(self, obj):
        return obj.muscles_secondary.values('id', 'name', 'is_front')

    def get_equipment(self, obj):
        return obj.equipment.values('id', 'name')

    def get_variations(self, obj):
        return obj.variations.values('id', 'name')
