from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import EndingListSerializer, EndingSerializer, MovieListSerializer, MovieSerializer
from .models import Ending, Movie


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def ending_list(request):
    if request.method == 'GET':
        endings = get_list_or_404(Ending)
        serializer = EndingListSerializer(endings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EndingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def ending_detail(request, article_pk):
    ending = get_object_or_404(Ending, pk=article_pk)

    if request.method == 'GET':
        serializer = EndingSerializer(ending)
        return Response(serializer.data)

@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET',])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)