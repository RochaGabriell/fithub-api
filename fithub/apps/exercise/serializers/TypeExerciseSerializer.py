from rest_framework import serializers

from fithub.apps.exercise.models import TypeExercise


class TypeExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeExercise
        fields = [
            "id",
            "name",
        ]
