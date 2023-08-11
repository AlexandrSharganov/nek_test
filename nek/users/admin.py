from django.contrib import admin

from .models import Follow


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Админка подписок"""

    list_display = (
        'author', 'user',
    )
    search_fields = (
        'user',
    )
    list_filter = ('user',)
