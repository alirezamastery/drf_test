from django.core.management import BaseCommand

from m2m_through.models import Marathon, Challenge, MarathonChallenge


class Command(BaseCommand):

    def handle(self, *args, **options):
        m1 = Marathon.objects.get(pk=1)
        c1 = Challenge.objects.first()
        m1.challenges.filter(marathon__challenges=c1)
        MarathonChallenge.objects.filter(marathon=m1, challenge=c1).exists()

