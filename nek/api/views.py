from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import mixins, viewsets, views, status
from rest_framework.response import Response
from django.db.utils import IntegrityError

from blog.models import Post
from blog.serializers import PostSerializer, ReadedPostSerializer
from users.models import Follow

from .pagination import CustomPostPagination
from .permissions import OwnerOrReadOnly


class PostViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """Вьюсет создания, удаления, получения списка постов или отдельного поста."""
    
    serializer_class = PostSerializer
    pagination_class = CustomPostPagination
    permission_classes = (OwnerOrReadOnly,)
    
    def get_queryset(self):
        """Выбираем queryset для работы с постами."""
        if self.action == 'list':
            user = get_object_or_404(User, username=self.request.user)
            subscribes = Follow.objects.filter(user=user).values('author')
            return Post.objects.filter(author__pk__in=subscribes)
        return Post.objects.select_related('author').all()
    
    def perform_create(self, serializer):
        """Добавляем автора при создании поста."""
        serializer.save(
            author=self.request.user,
            blog=self.request.user.blog
        )


class APIReaded(views.APIView):
    """Вьюшка для создания/удаления подписки."""

    def post(self, request, pk=None):
        """Создание подписки."""
        user = get_object_or_404(User, username=request.user)
        post = get_object_or_404(Post, pk=pk)
        try:
            serializer = ReadedPostSerializer(data={"user": user.pk, "post": post.pk})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        except IntegrityError:
            return Response(
                serializer.error,
                status=status.HTTP_400_BAD_REQUEST
            )