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
    # readed = models.ManyToManyField(
    #     User,
    #     on_delete=models.CASCADE,
    # )
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-pub_date',)
        
    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(
        verbose_name='title',
        max_length=50,
    )
    description = models.CharField(
        verbose_name='description',
        max_length=250,
    )
    subscriptions = models.ManyToManyField(
        User,
        related_name='subscription',
        blank=True,
        verbose_name='subscriptions',
    )
    author = models.ForeignKey(
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
