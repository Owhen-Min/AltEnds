# Generated by Django 4.2.16 on 2024-11-18 02:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('director', models.TextField()),
                ('openYear', models.IntegerField()),
                ('genre', models.TextField()),
                ('plot', models.TextField()),
                ('poster', models.ImageField(blank=True, upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Ending',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Movie', to='moviearticles.movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ending', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ending_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviearticles.ending')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
