from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    date_joined = models.DateField()

    def __str__(self):
        return f'{self.username}'


class Group(models.Model):
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.title}'

# Group.objects.filter().values_list()
