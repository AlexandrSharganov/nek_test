from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from users.models import User

from blog.models import Post, ReadedPost


class BlogSerializer(serializers.ModelSerializer):
    """Сериализатор получения блога."""

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'blog'
        )


class ReadedPostSerializer(serializers.ModelSerializer):
    """Сериализатор получения прочитанных постов."""

    read_status = serializers.SerializerMethodField()

    class Meta:
        model = ReadedPost
        fields = ('id', 'user', 'post', 'read_status',)
        validators = [
            UniqueTogetherValidator(
                queryset=ReadedPost.objects.all(),
                fields=('user', 'post'),
            )
        ]

    def get_read_status(self, obj):
        return ReadedPost.objects.filter(
            post=obj.post,
            user=obj.user
        ).exists()


class UserPostSerializer(serializers.ModelSerializer):
    """Сериализатор информации об авторе поста."""

    class Meta:
        model = User
        fields = (
            'id', 'username',
        )


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор получения постов."""

    author = UserPostSerializer(read_only=True)
    read_status = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'text', 'pub_date', 'author', 'blog', 'read_status'
        )

    def get_read_status(self, obj):
        return ReadedPost.objects.filter(
            post=obj,
            user=self.context['request'].user
        ).exists()
