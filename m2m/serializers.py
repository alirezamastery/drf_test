from pprint import pprint

from rest_framework import serializers

from .models import User, Group


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        depth = 1


class GroupWriteSerializer(serializers.ModelSerializer):
    users = serializers.ListSerializer(child=serializers.IntegerField(), allow_empty=True, required=False)

    class Meta:
        model = Group
        fields = '__all__'

    def to_representation(self, instance):
        users = UserSerializer(instance.users.all(), many=True).data
        result = {
            'title': instance.title,
            'users': users
        }
        return GroupReadSerializer(instance).data

    @staticmethod
    def validate_users(value):
        print(type(value))
        users = []
        for i in value:
            try:
                user = User.objects.get(pk=i)
            except User.DoesNotExist:
                raise serializers.ValidationError(f'no user with id {i}')
            users.append(user)

        return users

    def update(self, instance, validated_data):
        users = validated_data.pop('users', None)
        super().update(instance, validated_data)
        if users is not None:
            instance.users.set(users)
        return instance
