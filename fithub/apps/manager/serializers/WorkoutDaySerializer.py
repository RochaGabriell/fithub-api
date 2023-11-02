from rest_framework import serializers

from fithub.apps.manager.models import WorkoutDay


class WorkoutDaySerializer(serializers.ModelSerializer):

    class Meta:
        
        model = WorkoutDay
        fields = "__all__"
