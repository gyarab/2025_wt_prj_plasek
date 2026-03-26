from django.db import models

# Create your models here.
class Album(models.Model):
	title = models.CharField(max_length=255)
	artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)
	producer = models.CharField(max_length=255)
	release_date = models.DateField()
	genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
	mb_id = models.PositiveSmallIntegerField()
	discogs_url = models.CharField()
	lastfm_url = models.CharField()

class Track(models.Model):
	title = models.CharField(max_length=255)
	artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)
	producer = models.ForeignKey('Producer', on_delete=models.SET_NULL, null=True)
	release_date = models.DateField()
	genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
	mb_id = models.PositiveSmallIntegerField()
	album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True)

class Artist(models.Model):
	name = models.CharField(max_length=255)
	mb_id = models.PositiveSmallIntegerField()
	discogs_url = models.CharField()
	lastfm_url = models.CharField()

class Producer(models.Model):
	name = models.CharField(max_length=255)
	mb_id = models.PositiveSmallIntegerField()
	discogs_url = models.CharField()
	lastfm_url = models.CharField()

class Genre(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)	

class Release(models.Model):
	name = models.CharField(max_length=255)
	release_media = models.CharField(max_length=255)
	album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True)
	single = models.ForeignKey('Track', on_delete=models.SET_NULL, null=True)
	discogs_url = models.CharField()
	lastfm_url = models.CharField()