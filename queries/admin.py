from django.contrib import admin

from .models import Parent, Child , SelfReference

class SelfReferenceAdmin(admin.ModelAdmin):
    list_display = ['name' , 'pk']

admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(SelfReference,SelfReferenceAdmin)
