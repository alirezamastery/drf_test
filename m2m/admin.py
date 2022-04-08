from django.contrib import admin

from .models import Group, User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'date_joined']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_users']

    @admin.display()
    def display_users(self, obj):
        return ' | '.join(f'{user.username} - {user.date_joined}' for user in obj.users.all())


admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)
