from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, PostCommentsAPIView

router = DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<post_id>/post-view', PostCommentsAPIView.as_view(), name='post-comment-view')
]
