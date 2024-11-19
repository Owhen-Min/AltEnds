from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from django.shortcuts import get_object_or_404
from .serializers import UserProfileSerializer

@api_view(['GET'])
def GetProfile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserProfileSerializer(user)
    return Response(data=serializer.data)
