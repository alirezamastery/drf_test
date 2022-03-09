from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone


# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='category', null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    body = models.TextField()

    status = models.BooleanField(default=False)

    image = models.ImageField(blank=True, default=True)

    favorite = models.BooleanField(default=False)

    published = models.DateTimeField(default=timezone.now)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    category = models.ManyToManyField(Category, )

    def __str__(self):
        return self.title