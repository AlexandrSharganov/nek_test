from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from users.models import User

from blog.models import Post, Blog, ReadedPost


class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = (
            'id', 'title', 'blog'
        )


class ReadedPostSerializer(serializers.ModelSerializer):
    
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
    """Сериализатор получения пользователей."""

    class Meta:
        model = User
        fields = (
            'id', 'username',
        )


class PostSerializer(serializers.ModelSerializer):
    
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
        
class PostCreateSerializer(serializers.ModelSerializer):
    
    author = UserPostSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = (
            'id', 'title', 'text', 'author'
        )
