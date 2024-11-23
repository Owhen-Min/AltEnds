from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'user', 'user_nickname', 'title', 'content', 'view', 'like_users', 'comment_set' )


class ArticleSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)
        
class CommentSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user_id', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article_id', 'user_id', )
