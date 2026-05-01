"""Serializers for API endpoints."""

from rest_framework import serializers

from posts.models import Comment, Group, Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for posts."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        """Meta configuration for Post serializer."""

        model = Post
        fields = '__all__'
        read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for groups."""

    class Meta:
        """Meta configuration for Group serializer."""

        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for comments."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        """Meta configuration for Comment serializer."""

        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post')
