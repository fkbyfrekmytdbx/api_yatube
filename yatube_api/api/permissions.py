"""Custom API permission classes."""

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Allow edits only for object authors."""

    def has_object_permission(self, request, view, obj):
        """Grant read for all, write for author only."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
