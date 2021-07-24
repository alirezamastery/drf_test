from django.db import models


class Example(models.Model):
    title = models.CharField(max_length=200, default='')
