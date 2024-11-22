from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.db.models import Count
from django.http import JsonResponse


from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import EndingListSerializer, EndingSerializer, MovieListSerializer, MovieSerializer, CommentSerializer
from accounts.serializers import UserRankingSerializer
from .models import Ending, Movie, Comment
from openai import OpenAI
from django.contrib.auth import get_user_model


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
    
@api_view(['GET', 'POST'])
def comment_list(request, ending_pk):
    if request.method == 'GET':
        comments = get_list_or_404(Comment, ending_id=ending_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        ending = get_object_or_404(Ending, pk=ending_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=request.user, ending_id=ending)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['POST',])
def generate_alt_ending(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user_prompt = request.data.get('prompt','')
    prev_alt_ending = request.data.get('content','')
    print(prev_alt_ending)
    client = OpenAI(api_key=settings.SECRET_KEY)
    movie_title = movie.title
    movie_plot = movie.plot

    if not prev_alt_ending:
        prompt_for_gpt = f"Plot summary: {movie_plot}\n\nGenerate an alternative ending for the movie {movie_title}. The alternative ending should diverge from the original conclusion with the given environment after. You will answer full plot of alternative ending by user input. Return plot only. If user input is irrelevant with movie, than return error message. PLEASE ANSWER IN KOREAN."        
    else:
        prompt_for_gpt = f"Plot summary: {movie_plot}\n\nYour Client is not content with your output. Generate an alternative ending for the movie {movie_title} again. The alternative ending(your result) should include the feedback from your client. You will answer full plot of alternative ending. Return plot only. If user input is irrelevant with movie, than return error message. PLEASE ANSWER IN KOREAN. The alternative ending you created is below. If previous alternative ending has error message, then you can skip it.\n\n{prev_alt_ending}"        
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

@api_view(['POST'])
def likes(request, ending_pk):
    ending = get_object_or_404(Ending, pk=ending_pk)
    if request.user in ending.like_users.all():
        ending.like_users.remove(request.user)
        ending.save()
        is_liked = False
    else:
        ending.like_users.add(request.user)
        ending.save()
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return Response(context)

@api_view(['GET'])
def GetUserRanking(request):
    user_ranking = (
        Ending.objects.values("user_id__id",)
        .annotate(total_likes=Count("like_users"))
        .order_by("-total_likes")[:3]
    )
    User = get_user_model()
    user_dict = dict()
    for rank, user in enumerate(user_ranking):
        user_instance = get_object_or_404(User, pk=user['user_id__id'])
        user_dict[rank+1] = {
            'user_name': user_instance.nickname,
            'total_likes': user['total_likes'],
            'user_id': user['user_id__id']
            }
    return JsonResponse(user_dict, safe=True)


@api_view(['GET'])
def GetEndingRanking(request):
    most_liked_article = (
        Ending.objects.annotate(like_count=Count("like_users"))
        .order_by("-like_count")[:6]
    )
    ending_dict = dict()

    for rank, article in enumerate(most_liked_article):
        ending_dict[rank+1] = {
            'movie': article.movie_id.title,
            'prompt': article.prompt,
            'like_count': article.like_count,
            'ending_id': article.id
        }
    
    return JsonResponse(ending_dict, safe=True)
