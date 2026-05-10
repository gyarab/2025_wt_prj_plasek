from django.db import models

# Create your models here.
class Album(models.Model):
	title = models.CharField(max_length=255)
	artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)
	release_date = models.DateField()
	genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
	mb_id = models.UUIDField()
	discogs_url = models.CharField(null=True)
	lastfm_url = models.CharField(null=True)

class Track(models.Model):
	title = models.CharField(max_length=255)
	artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)
	release_date = models.DateField()
	genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
	mb_id = models.UUIDField()
	album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True)

class Artist(models.Model):
	name = models.CharField(max_length=255)
	mb_id = models.UUIDField()
	discogs_url = models.CharField(null=True)
	lastfm_url = models.CharField(null=True)

class Producer(models.Model):
	name = models.CharField(max_length=255)
	mb_id = models.UUIDField()
	discogs_url = models.CharField(null=True)
	lastfm_url = models.CharField(null=True)

class Genre(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)	

class Release(models.Model):
	name = models.CharField(max_length=255)
	release_media = models.CharField(max_length=255)
	album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True)
	single = models.ForeignKey('Track', on_delete=models.SET_NULL, null=True)
	mb_id = models.UUIDField()
	discogs_url = models.CharField(null=True)
	lastfm_url = models.CharField(null=True)