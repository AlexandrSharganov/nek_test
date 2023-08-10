from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model."""
    
    title = models.CharField(
        verbose_name='title',
        max_length=50,
    )
    text = models.CharField(
        verbose_name='text',
        max_length=140,
        null=True,
        blank=True,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        verbose_name='author',
        related_name='post',
        on_delete=models.CASCADE,
    )
    blog = models.ForeignKey(
        'Blog',
        verbose_name='blog',
        related_name='post',
        on_delete=models.CASCADE,
        # для создания тестовой базы
        null=True,
        blank=True,
    )
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-pub_date',)
        
    def __str__(self):
        return self.title


class Blog(models.Model):
    """Blog model."""
    title = models.CharField(
        verbose_name='title',
        max_length=50,
    )
    description = models.CharField(
        verbose_name='description',
        max_length=250,
    )
    author = models.OneToOneField(
        User,
        related_name='blog',
        verbose_name='author',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

    def __str__(self):
        return self.title


class ReadedPost(models.Model):
    """ReadedPost model."""
    
    user = models.ForeignKey(
        User,
        related_name='user_readed',
        on_delete=models.CASCADE,
        verbose_name='user readed',
    )
    post = models.ForeignKey(
        Post,
        related_name='post_readed',
        on_delete=models.CASCADE,
        verbose_name='post readed',
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'post'],
                name='unique_post'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('post')),
                name='check_self_post'),
        ]