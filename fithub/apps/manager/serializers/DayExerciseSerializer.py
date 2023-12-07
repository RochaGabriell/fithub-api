from rest_framework import serializers

from fithub.apps.manager.models import DayExercise


class DayExerciseSerializer(serializers.ModelSerializer):

    exercisesDetails = serializers.SerializerMethodField()

    class Meta:

        model = DayExercise
        fields = [
            'id',
            'day_list',
            'exercise',
            'exercisesDetails',
            'series',
            'repetitions',
            'weight',
            'created_at',
            'updated_at',
        ]

    def get_exercisesDetails(self, obj):
        return {
            'id': obj.exercise.id,
            'name': obj.exercise.name,
        }
