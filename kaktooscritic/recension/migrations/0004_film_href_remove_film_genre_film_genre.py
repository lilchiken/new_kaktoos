# Generated by Django 4.1.5 on 2023-01-30 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recension', '0003_alter_film_author_alter_film_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='href',
            field=models.TextField(default='https://www.kinopoisk.ru/film/361/', max_length=100),
        ),
        migrations.RemoveField(
            model_name='film',
            name='genre',
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(related_name='genres', to='recension.genre'),
        ),
    ]
