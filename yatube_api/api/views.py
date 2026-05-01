"""Viewsets for API endpoints."""

from django.shortcuts import get_object_or_404
from rest_framework import mixins, permissions, viewsets

from posts.models import Group, Post

from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """CRUD operations for posts."""

    queryset = Post.objects.select_related('author', 'group').all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        """Save post author from current user."""
        serializer.save(author=self.request.user)


class GroupViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """Read-only operations for groups."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """CRUD operations for comments under a post."""

    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)

    def get_post(self):
        """Return parent post from URL kwargs."""
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get_queryset(self):
        """Return comments for the parent post."""
        return self.get_post().comments.select_related('author').all()

    def perform_create(self, serializer):
        """Save author and parent post for new comment."""
        serializer.save(
            author=self.request.user,
            post=self.get_post(),
        )
