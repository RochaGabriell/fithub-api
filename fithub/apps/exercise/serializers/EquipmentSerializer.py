from rest_framework import serializers

from fithub.apps.exercise.models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Equipment
        fields = [
            "id",
            "name",
        ]
