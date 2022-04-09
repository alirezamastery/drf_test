from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import BlogPost


# With object permissions support
class BlogPostAdmin(GuardedModelAdmin):
    pass


admin.site.register(BlogPost, BlogPostAdmin)
