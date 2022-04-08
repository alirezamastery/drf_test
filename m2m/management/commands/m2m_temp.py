from django.core.management import BaseCommand
from django.db.models import Count

from ...models import Group, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        users_qs = User.objects.filter(date_joined__range=['2022-03-15', '2022-03-18'])
        user_1 = User.objects.get(username='user_1')
        user_2 = User.objects.get(username='user_2')
        user_3 = User.objects.get(username='user_3')
        user_6 = User.objects.get(username='user_6')
        user_7 = User.objects.get(username='user_7')
        user_9 = User.objects.get(username='user_9')
        # print(users_qs)
        users = list(users_qs)
        # print(users)
        user_list = [user_1, user_2]
        # user_list = [user_6, user_7]
        qs = Group.objects.filter(users__in=user_list)
        print(qs)
        print(qs.query)
        print()
        qs = Group.objects \
            .filter(users__in=user_list) \
            .alias(nusers=Count('users')) \
            .filter(nusers=len(user_list))
        print(qs.query)
        print(qs)
