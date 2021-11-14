from pprint import pprint

from django.test import TestCase
from rest_framework.test import APIClient, APITransactionTestCase
from django.urls import reverse
from ..models import *


class TestAPIGroupChange(APITransactionTestCase):
    # fixtures = ['chat/tests/fixtures/group_users.json']

    def setUp(self) -> None:
        self.client = APIClient()
        self.url_base = reverse('bulk_update:invoice-items-list')
        # self.url_base = 'http://127.0.0.1:8000/api/bulk/invoice-items/'
        print(f'{self.url_base = }')
        self.invoice = Invoice.objects.create(number=1)

    def test_list_create(self):
        payload = []
        for i in range(100000):
            payload.append({
                'invoice': self.invoice.pk,
                # 'invoice': 2,
                'price':   i
            })
        response = self.client.post(self.url_base, data=payload, format='json')
        print(response)
        # pprint(response.json())
