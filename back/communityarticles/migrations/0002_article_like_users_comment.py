# Generated by Django 4.2.16 on 2024-11-19 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communityarticles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like_users',
            field=models.ManyToManyField(default=None, related_name='like_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communityarticles.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]