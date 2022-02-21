from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<id>\d+)/comments', CommentViewSet,
                basename="comments")
urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments', CommentViewSet),
    path('posts/<int:post_id>/comments/<comment_id>', CommentViewSet)
]
