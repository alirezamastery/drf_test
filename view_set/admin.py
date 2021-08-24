from django.contrib import admin

from .models import Example, Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'group_id', 'file_type']


admin.site.register(Example)
admin.site.register(Message, MessageAdmin)
