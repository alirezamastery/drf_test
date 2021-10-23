from django.contrib import admin

from .models import *


class MarathonChallengeInline(admin.TabularInline):
    model = MarathonChallenge


class MarathonAdmin(admin.ModelAdmin):
    inlines = [MarathonChallengeInline]


admin.site.register(Marathon, MarathonAdmin)
admin.site.register(MarathonChallenge)
admin.site.register(Challenge)
