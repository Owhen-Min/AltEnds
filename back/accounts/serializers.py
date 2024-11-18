from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=20, required=True)
    def save(self, request):
        user = super().save(request)
        nickname = self.initial_data.get('nickname')
        if nickname:
            user.nickname = nickname
            user.save()
        return user
