# Generated by Django 4.2.16 on 2024-11-26 11:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moviearticles', '0002_alter_comment_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ending',
            name='dislike_users',
            field=models.ManyToManyField(default=None, related_name='dislike_endings', to=settings.AUTH_USER_MODEL),
        ),
    ]
