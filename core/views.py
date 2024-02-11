from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, PostCommentsViewSerializer
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class PostCommentsAPIView(generics.ListAPIView):
    serializer_class = PostCommentsViewSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Post.objects.filter(id=post_id)
