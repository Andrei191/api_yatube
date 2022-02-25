from rest_framework import serializers

from posts.models import Comment, Group, Post, User  # isort:skip


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('title', 'slug', 'description', 'posts')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date',
                  'author', 'image', 'group', 'comments')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'posts', 'comments',)
