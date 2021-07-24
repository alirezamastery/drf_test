from rest_framework import serializers
from .models import Parent, Child, SelfReference


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'


class SelfReferenceSerializer(serializers.ModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(queryset=Parent.objects.all(),
                                                   allow_null=True, required=False)

    class Meta:
        model = SelfReference
        fields = ['name' ,'parent', 'parent_id']
        # fields ='__all__'
        depth = 1
    # def to_representation(self, instance):
    #     res = super().to_representation(instance)
    #     res['pp'] = 'opp'
    #     return res


class FieldNameChangeSerializer(serializers.ModelSerializer):
    some_name = serializers.SerializerMethodField('get_name')

    class Meta:
        model = SelfReference
        fields = '__all__'

    def get_name(self, obj):
        return obj.name
