from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

from blog.models import Blog, Post


@receiver(post_save, sender=User)
def save_or_create_create(sender, instance, created, **kwargs):
    """Создание блога вместе с пользователем."""
    if created:
        title = f'{instance.username}`s blog'
        Blog.objects.create(author=instance, title=title)


class Follow(models.Model):
    """Модель подписок на пользователей."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='follower'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='following'
    )

    class Meta:
        verbose_name = 'Follow'
        verbose_name_plural = 'Follows'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_follow'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('author')),
                name='check_self_following'),
        ]

    def __str__(self):
        return f'{self.user} {self.author}'
    