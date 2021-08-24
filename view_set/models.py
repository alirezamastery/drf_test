from django.db import models
import uuid


class Example(models.Model):
    title = models.CharField(max_length=200, default='')


class Message(models.Model):
    body = models.CharField(max_length=200, default=uuid.uuid4)
    group_id = models.SmallIntegerField(default=35)
    file_type = models.SmallIntegerField(default=0)
