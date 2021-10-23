from django.db import models
from django.utils import timezone


class Marathon(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    challenges = models.ManyToManyField('Challenge', through='MarathonChallenge')

    def __str__(self):
        return f'{self.pk} - {self.title}'


class MarathonChallenge(models.Model):
    marathon = models.ForeignKey('Marathon', on_delete=models.CASCADE)
    challenge = models.ForeignKey('Challenge', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    start_date = models.DateTimeField(default=timezone.now())

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['marathon', 'challenge'],
                name='unique_marathon_challenge'
            )
        ]


class Challenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
