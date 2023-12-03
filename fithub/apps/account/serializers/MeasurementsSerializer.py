from rest_framework import serializers

from fithub.apps.account.models import Measurements


class MeasurementsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Measurements
        fields = "__all__"
