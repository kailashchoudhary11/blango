from django.contrib import admin
from blog.models import Post, Tag, Comment

# Register your models here.

admin.site.register(Tag)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
 # exclude = ["slug"] # Prevents us from editing these fields in the admin site
  list_display = ["slug", "published_at", ]

admin.site.register(Comment)