from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Follow

from .serializers import FollowSerializer


class APIFollow(APIView):
    """Вьюшка для создания/удаления подписки."""

    def post(self, request, pk=None):
        """Создание подписки."""
        user = get_object_or_404(User, username=request.user)
        author = get_object_or_404(User, pk=pk)
        serializer = FollowSerializer(data={"user": user.pk, "author": pk})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def delete(self, request, pk=None):
        """Удаление подписки."""
        user = get_object_or_404(User, username=request.user)
        follow = get_object_or_404(Follow, user=user, author=pk)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
