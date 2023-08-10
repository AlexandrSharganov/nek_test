from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import APIFollow

from .views import PostViewSet, APIReaded


app_name = 'api'

router = DefaultRouter()

router.register('post', PostViewSet, basename='post')

urlpatterns = [
    path('v1/users/<int:pk>/subscribe/', APIFollow.as_view()),
    path('v1/post/<int:pk>/readed/', APIReaded.as_view()),
    path('v1/', include(router.urls)),
]

