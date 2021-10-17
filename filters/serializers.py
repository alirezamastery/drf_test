from rest_framework import serializers

from .models import Marathon


class MarathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marathon
        fields = '__all__'

    def validate(self, attrs):
        data = super().validate(attrs)
        print(data)
        return data
