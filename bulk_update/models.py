from django.db import models


class Invoice(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return f'{self.number}'

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.invoice.number} - {self.price}'
