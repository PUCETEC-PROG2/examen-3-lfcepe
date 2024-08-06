from django.db import models

# Create your models here.

class Artist(models.Model):
    artist_name = models.CharField(max_length=100, null = False)
    artist_country = models.CharField(max_length=50, null = False)
    artist_biography = models.TextField(null = False)
    picture = models.ImageField(upload_to='artist_images')

    def __str__(self) -> str:
        return self.artist_name
    
class Album(models.Model):
    album_title = models.CharField(max_length=80, null=False)
    year = models.CharField(max_length=4, null=False)
    MUSIC_GENDER = {
        ('Musica Clasica', 'Musica Clasica'),
        ('Blues', 'Blues'),
        ('R&B', ' Rhythm and blues'),
        ('Jzz', 'Jazz'),
        ('Soul', 'Soul'),
        ('Funk', 'Funk'),
        ('Rock', 'Rock'),
        ('Pop', 'Pop'),
        ('Rap', 'Rap'),
        ('RGG', 'Reggae'),
        ('Rt', 'Reguetón'),
    }
    gender = models.CharField(max_length=50, choices=MUSIC_GENDER, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_details = models.TextField(null = False)
    covers = models.ImageField(upload_to='covers_images')

    def __str__(self) -> str:
        return f'{self.album_title}-{self.year}'