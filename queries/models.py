import uuid

from django.db import models


class Parent(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Child(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.unique_id)


class SelfReference(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('SelfReference', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.pk} | {self.name}'
