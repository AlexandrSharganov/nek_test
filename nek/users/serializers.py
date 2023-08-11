from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Follow


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
