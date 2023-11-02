from rest_framework import serializers

from fithub.apps.manager.models import DayExercise


class DayExerciseSerializer(serializers.ModelSerializer):

    class Meta:

        model = DayExercise
        fields = "__all__"
