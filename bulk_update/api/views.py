from rest_framework.viewsets import ModelViewSet

from ..serializers import *


class InvoiceItemViewSet(ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            for d in kwargs['data']:
                invoice_id = d.pop('invoice')
            invoice = Invoice.objects.get(pk=invoice_id)

            kwargs["many"] = True
        return super().get_serializer(*args, **kwargs)
