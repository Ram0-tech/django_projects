from django.db import models

class Movie(models.Model):
    image = models.ImageField(upload_to='movie')
    movie_name=models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField ()

