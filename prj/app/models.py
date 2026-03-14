from django.db import models

# Create your models here.
class Album(models.Model):
	title = models.CharField(max_length=255)
	artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)
	producer = models.CharField(max_length=255)
	release_date = models.DateField()
	mb_id = models.PositiveSmallIntegerField()
	discogs_url = models.CharField()
	lastfm_url = models.CharField()

class Artist(models.Model):
	name = models.CharField(max_length=255)
	mb_id = models.PositiveSmallIntegerField()
	discogs_url = models.CharField()
	lastfm_url = models.CharField()
	
