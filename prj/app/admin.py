from django.contrib import admin

# Register your models here.
from .models import Album, Track, Artist, Producer, Genre, Release

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
	pass

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
	pass

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
	pass

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
	pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	pass

@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
	pass