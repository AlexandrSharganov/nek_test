from django.contrib import admin

from .models import Post, Blog, ReadedPost


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Админка пользователей."""

    list_display = (
        'id', 'title', 'text', 'pub_date', 'author',
    )
    
    list_display_links = ('id', 'title')
    empty_value_display = '-пусто-'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Админка пользователей."""

    list_display = (
        'id', 'title', 'description',
    )
    list_display_links = ('id', 'title')
    empty_value_display = '-пусто-'


admin.site.register(ReadedPost)