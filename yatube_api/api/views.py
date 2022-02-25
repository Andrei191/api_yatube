from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets

from .permissions import IsAuthorOrReadOnlyPermission  # isort:skip
from .serializers import CommentSerializer, GroupSerializer  # isort:skip
from .serializers import PostSerializer  # isort:skip
from posts.models import Group, Post  # isort:skip


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsAuthorOrReadOnlyPermission)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsAuthorOrReadOnlyPermission)

    def get_queryset(self):
        post_id = self.kwargs.get("id")
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get("id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)
