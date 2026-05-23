from django.db import models

from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    genre = models.CharField(max_length=100, verbose_name='Género')
    director_name = models.CharField(max_length=150, verbose_name='Director')
    publication_year = models.IntegerField(verbose_name='Año de publicación')
    synopsis = models.TextField(verbose_name='Sinopsis')

    class Meta:
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'
        ordering = ['-publication_year', 'title']

    def __str__(self):
        return f'{self.title} - {self.publication_year}'