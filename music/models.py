from django.conf import settings
from django.db import models

import  random
import  string
import math

f = random.choice([i for  i in range(85)])
g = random.choice([j for j in string.ascii_letters ])
# Create your models here.
class Album(models.Model):
    #user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='album', on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField(blank=True,null=True,upload_to=f'musicas/{f}/{g}')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album,related_name='songs', on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(blank=True,null=True,default='',upload_to=f"musicatsong/{f}/{g}")
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title