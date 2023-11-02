from rest_framework import serializers

from fithub.apps.manager.models import Workout


class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:

        model = Workout
        fields = "__all__"
