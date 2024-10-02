from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
  # path("posts", PostListView.as_view(), name='post-list'),
  path('', include(router.urls)),
]