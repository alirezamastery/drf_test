from pprint import pprint

from django.db import IntegrityError
from rest_framework import serializers

from .models import InvoiceItem, Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceItemListSerializer(serializers.ListSerializer):

    def validate(self, attrs):
        # print('\n*** InvoiceItemListSerializer | attrs inside validate:')
        # print(attrs)
        # print()
        return attrs

    def create(self, validated_data):
        invoice_items = [self.child.Meta.model(**item) for item in validated_data]
        try:
            return self.child.Meta.model.objects.bulk_create(invoice_items)
        except IntegrityError as e:
            raise serializers.ValidationError(e)


class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = '__all__'
        list_serializer_class = InvoiceItemListSerializer

    def validate(self, attrs):
        # print('\n*** InvoiceItemSerializer | attrs inside validate:')
        # print(attrs)
        # print()
        return super().validate(attrs)
