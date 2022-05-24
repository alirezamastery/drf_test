from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=255)


class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='messages')
    body = models.TextField(default='')
