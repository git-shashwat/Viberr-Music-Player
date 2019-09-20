from django.db import models
# To generate url corresponding to view.
from django.urls import reverse

# from django.urls import reverse
class Album(models.Model):
    artist = models.CharField(max_length = 250, verbose_name = 'Artist')
    album_title = models.CharField(max_length = 500, verbose_name = 'Title')
    genre = models.CharField(max_length = 100, verbose_name = 'Genre')
    album_logo = models.FileField(verbose_name='Album Cover')

    def get_absolute_url(self):
        return reverse("music:detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.album_title + ', ' + self.artist

    def __dir__(self):
        return ['artist', 'album_title', 'genre']

    def save(self, *args, **kwargs):
        for field in ['artist','album_title','genre']:
            val = getattr(self, field, False)
            if val:
                setattr(self, field, val.upper())
                super().save(*args, **kwargs)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete= models.CASCADE)
    song_file = models.FileField(verbose_name='Upload Song')
    file_type = models.CharField(max_length = 10, verbose_name='File Type')
    song_title = models.CharField(max_length = 250, verbose_name='Song Title')
    is_favorite = models.BooleanField(default=False, verbose_name='Favorite')

    def get_absolute_url(self):
        return reverse("music:detail", kwargs={"pk": self.album.pk})
    
    def __str__(self):
        return self.song_title

    def save(self, *args, **kwargs):
        for field in ['file_type','song_title']:
            val = getattr(self, field, False)
            if val:
                setattr(self, field, val.upper())
                super().save(*args, **kwargs)
