from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=20, required=True)
    def save(self, request):
        user = super().save(request)
        nickname = self.initial_data.get('nickname')
        first_name = self.cleaned_data.get('firstname')
        if nickname and first_name:
            user.nickname = nickname
            user.first_name = first_name
            user.save()
        return user

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'nickname', 'profile_picture', 'join_date', 'token')
        read_only_fields = ('pk', 'username', 'join_data', )

class UserRankingSerializer(ModelSerializer):
    total_likes = serializers.IntegerField()
    class Meta:
        model = User
        fields = ('pk', 'nickname', 'total_likes')