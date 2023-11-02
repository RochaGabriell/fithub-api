from rest_framework import serializers

from fithub.apps.exercise.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"

    # def to_representation(self, instance):
    #     # Inplementar HATEOAS (Hypermedia as the Engine of Application State)
    #     data = super().to_representation(instance)
    #     data['links'] = {
    #         'self': reverse('exercise-detail', kwargs={'pk': instance.id}),
    #         'update': reverse('exercise-update', kwargs={'pk': instance.id}),
    #         'delete': reverse('exercise-delete', kwargs={'pk': instance.id}),
    #         'variations': reverse('exercise-variations', kwargs={'pk': instance.id}),
    #     }
    #     return data
