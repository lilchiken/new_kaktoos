from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Genre(models.Model):
    title = models.CharField(
        max_length=50,
        null=False
    )

    def __str__(self):
        return self.title


class Film(models.Model):
    title = models.CharField(
        max_length=150,
        null=False
    )
    genre = models.ManyToManyField(
        Genre
    )
    pub_date_film = models.DateField(
        blank=True,
        null=True
    )
    author = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='recension/',
        blank=True,
        null=True
    )
    href = models.TextField(
        max_length=100,
        default='https://www.kinopoisk.ru/film/361/'
    )


class Recension(models.Model):
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name='recension',
        null=True
    )
    small_text = models.CharField(
        max_length=70
    )
    text = models.CharField(
        max_length=5000
    )
    pub_date = models.DateField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-pub_date']


class Grade(models.Model):
    recension = models.ForeignKey(
        Recension,
        on_delete=models.DO_NOTHING,
        related_name='grade',
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='grade',
        null=True,
        blank=True
    )
    grade = models.SmallIntegerField(
        null=True
    )
