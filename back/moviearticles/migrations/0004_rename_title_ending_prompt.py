# Generated by Django 4.2.16 on 2024-11-20 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviearticles', '0003_alter_movie_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ending',
            old_name='title',
            new_name='prompt',
        ),
    ]
