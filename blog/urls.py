from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import PostViewSet, CommentViewSet
from .views import PostViewSet, AddCommentView, ListCommentView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
# router.register(r'comments', CommentViewSet, basename = 'comment')

urlpatterns = [
  # path("posts", PostListView.as_view(), name='post-list'),
  path('', include(router.urls)),
  path('posts/<int:post_id>/comments/', ListCommentView.as_view(), name='list-comment'),
  path('comments/add', AddCommentView.as_view(), name='add-comment'),
]