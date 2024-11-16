from django.db import models
from django.conf import settings


class Article(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Movie_Article',
    )
    movie = models.ForeignKey("Movie", related_name='Movie', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.TextField()
    openYear = models.IntegerField()
    nation = models.CharField(max_length=50)
    genre = models.TextField()
    plot = models.TextField()
    poster = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True)