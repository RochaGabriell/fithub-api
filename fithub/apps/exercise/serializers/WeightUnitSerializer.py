from rest_framework import serializers

from fithub.apps.exercise.models import WeightUnit


class WeightUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightUnit
        fields = [
            "id",
            "name",
        ]
