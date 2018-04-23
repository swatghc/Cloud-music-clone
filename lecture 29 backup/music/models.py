# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


from django.db import models

# Create your models here.

# each var in class, create column in table

#  Re primarykey 1
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    #built-in string representation of a object
    def __str__(self):
        return self.album_title+" - "+ self.artist


class Song(models.Model):

    #  CASCADE: once album is deleted, all the song also deleted
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
