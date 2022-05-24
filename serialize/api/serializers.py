from rest_framework import serializers

from ..models import *


class MessageSerializer(serializers.Serializer):
    message = serializers.PrimaryKeyRelatedField(queryset=Message.objects.all())

    def validate(self, attrs):
        attrs['chaikin'] = 'chaikin'
        return attrs
