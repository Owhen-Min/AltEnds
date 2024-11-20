from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'user', 'user_nickname', 'title', 'content', 'view')


class ArticleSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'user','title','content', 'user_nickname','created_at', 'updated_at', 'view')
        read_only_fields = ('user',)
