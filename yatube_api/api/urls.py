"""URL routes for API v1."""

from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')

comments_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
comments_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('posts/<int:post_id>/comments/', comments_list, name='comments-list'),
    path(
        'posts/<int:post_id>/comments/<int:pk>/',
        comments_detail,
        name='comments-detail',
    ),
]
