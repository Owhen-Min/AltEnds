from rest_framework import serializers
from .models import Ending, Movie


class EndingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ending
        fields = ('id', 'title', 'content')


class EndingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ending
        fields = '__all__'
        read_only_fields = ('user',)

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster')
        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
