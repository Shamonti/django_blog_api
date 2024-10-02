from django.shortcuts import render

# Create your views here.
# from rest_framework.views import APIView
from rest_framework import viewsets, generics
# from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# class PostListView(APIView):
#   def get(self, request):
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

# class CommentViewSet(viewsets.ModelViewSet):
#   queryset = Comment.objects.all()
#   serializer_class = CommentSerializer

class AddCommentView(generics.CreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

class ListCommentView(generics.ListAPIView):
  serializer_class = CommentSerializer

  def get_queryset(self):
      post_id = self.kwargs['post_id']  # Extract the post ID from the URL
      return Comment.objects.filter(post__id=post_id)