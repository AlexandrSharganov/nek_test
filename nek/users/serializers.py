from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Follow


class MyUserSerializer(serializers.ModelSerializer):
    """Сериализатор получения пользователей."""    

    class Meta:
        model = User
        fields = (
            'email', 'id', 'username', 'first_name',
            'last_name',
        )


class MyUserCreateSerializer(serializers.ModelSerializer):
    """Сериализатор создания пользователей."""

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password',
        )


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор создания подписки."""

    class Meta:
        model = Follow
        fields = ('user', 'author')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'author'),
            )
        ]

    def validate(self, data):
        """Валидируем подписку на себя."""
        if data.get('user') == data.get('author'):
            raise serializers.ValidationError(
                'Нельзя подписаться на себя!')
        return data
