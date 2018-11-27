from django.contrib import admin
from backend.app.models import Post

class PostAdmin(admin.ModelAdmin):
    """Сообщения"""
    list_display = ("id", "user", "text", "twit", "like", "date")

admin.site.register(Post, PostAdmin)
