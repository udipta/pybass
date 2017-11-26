# from django.core.validators import RegexValidator

from django.contrib.auth.models import User
from django.db import models


class Album(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title


class Feedback(models.Model):
    # alpha = RegexValidator(r'^[a-zA-Z]*$', "Only alphabets are allowed.")

    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    presentation = models.CharField(max_length=20)
    collaboration = models.CharField(max_length=20)
    objectives = models.CharField(max_length=20)
    suggestion = models.CharField(max_length=500)

    def __str__(self):
        return self.fname


