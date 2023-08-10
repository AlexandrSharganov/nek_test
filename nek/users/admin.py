from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Follow


@admin.register(User)
class UserAdmin(UserAdmin):
    """Админка пользователей."""

    list_display = (
        'id', 'username', 'email', 'first_name',
        'last_name', 'password'
    )
    list_display_links = ('id', 'username')
    search_fields = ('username', 'email',)
    list_filter = ('email', 'username')
    empty_value_display = '-пусто-'
    

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Админка подписок"""

    list_display = (
        'author', 'user', 
    )
