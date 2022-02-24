from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = DefaultRouter()
router.register('v1/posts', PostViewSet)
router.register('v1/groups', GroupViewSet)
router.register(r'v1/posts/(?P<id>\d+)/comments', CommentViewSet,
                basename="comments")
urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
