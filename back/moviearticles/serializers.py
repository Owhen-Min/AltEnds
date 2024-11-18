from rest_framework import serializers
from .models import Ending


class EndingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ending
        fields = ('id', 'title', 'content')


class EndingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ending
        fields = '__all__'
        read_only_fields = ('user',)
