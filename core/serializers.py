from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostCommentsViewSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        return CommentSerializer(Post.objects.get(id=obj.id).post_comments.all(), many=True).data
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'body', 'created_at', 'updated_at', 'comments')
