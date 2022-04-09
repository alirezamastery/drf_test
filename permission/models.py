from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='')

    def __str__(self):
        return self.title
