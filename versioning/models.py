from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(default='versioning/blog')

    def __str__(self):
        return self.title
