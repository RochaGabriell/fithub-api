from rest_framework import serializers
from datetime import date

from fithub.apps.account.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):

    show_age = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['name',
                  'username',
                  'email',
                  'birth_date',
                  'sex',
                  'show_age',
                  ]

    def get_show_age(self, obj):
        today = date.today()
        return today.year - obj.birth_date.year - ((today.month, today.day) < (obj.birth_date.month, obj.birth_date.day))


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = [
            'id',
            'name',
            'username',
            'email',
            'birth_date',
            'sex',
            'password',
        ]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
