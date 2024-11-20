from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import EndingListSerializer, EndingSerializer, MovieListSerializer, MovieSerializer
from .models import Ending, Movie
from openai import OpenAI



# @permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def ending_list(request):
    if request.method == 'GET':
        endings = get_list_or_404(Ending)
        serializer = EndingListSerializer(endings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EndingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def ending_detail(request, ending_pk):
    ending = get_object_or_404(Ending, pk=ending_pk)

    if request.method == 'GET':
        ending.view += 1
        ending.save()
        serializer = EndingSerializer(ending)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        ending.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
    

@api_view(['POST',])
def generate_alt_ending(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user_prompt = request.data.get('prompt','')
    client = OpenAI(api_key=settings.SECRET_KEY)

    if not user_prompt:
        return Response({'error': 'Prompt is required.'}, status=400)
    
    movie_title = movie.title
    movie_plot = movie.plot

    prompt_for_gpt = f"Plot summary: {movie_plot}\n\nGenerate an alternative ending for the movie {movie_title}. The alternative ending should diverge from the original conclusion with the given environment after. You will answer full plot with alternative ending by user input. return only plots without 잡말. If user input is irrelevant with movie, than return error message. PLEASE ANSWER IN KOREAN."
    gpt_prompt = (f"{user_prompt}")
    
    try:
        # Send the prompt to GPT
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # You can use other engines if needed
            messages=[
                { "role": "system", 'content':prompt_for_gpt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=1500,
            n=1,
            temperature=1.0
        )
        gpt_response = response.choices[0].message.content
    except Exception as e:
        return Response({'error': f"Failed to communicate with GPT: {str(e)}"}, status=500)
    
    # Return the GPT response
    return Response({'alt_ending': gpt_response})