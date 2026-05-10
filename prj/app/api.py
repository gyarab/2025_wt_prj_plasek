from .models import Album, Artist
from ninja import NinjaAPI
import requests

api: NinjaAPI = NinjaAPI()

@api.get("/album")
def get_album_list(request):
	albums = Album.objects.all()
	output = []
	for a in albums:
		output.append({
			"id": a.pk,
			"title": a.title,
			"artist": a.artist.name
		})

	return {
		"status": "ok",
		"albums": output
	}

@api.get("/album/{album_id}")
def get_album(request, album_id: int):
	try:
		album = Album.objects.get(pk=album_id)
		return {
			"status": "ok",
			"id": album.pk,
			"title": album.title,
			"artist": album.artist.name,
			"producer": album.producer,
			"release_date": str(album.release_date),
			"genre": album.genre.name,
			"mb_id": album.mb_id,
			"discogs_url": album.discogs_url,
			"lastfm_url": album.lastfm_url
		}
	except Album.DoesNotExist:
		return 404, {
			"status": "not found"
		}

@api.post("/add_album")
def add_album(request, mb_id):
	try:
		mb_lookup = requests.get(f'https://musicbrainz.org/ws/2/release/{mb_id}?inc=artists&fmt=json').json()
		new_field = Album(
			title = mb_lookup['title'],
			artist = Artist.objects.get_or_create(
				name = mb_lookup['artist-credit'][0]['artist']['name'],
				defaults = {
					'mb_id': mb_lookup['artist-credit'][0]['artist']['id']
				})[0],
			release_date = mb_lookup['date'],
			mb_id = mb_id
		)

		new_field.save()

		return {
			"status": "success",
			"new_album": {
				"title": new_field.title,
				"aritst": new_field.artist.name,
				"release_date": str(new_field.release_date),
				"mb_id": mb_id
			}
		}
	except Exception as e:
		print(e)
		return {
			"status": "Internal Server Error"
		}

@api.post("/edit_album_id/{id}")
def edit_album_id(request, id, new_mb_id):
	try:
		mb_lookup = requests.get(f'https://musicbrainz.org/ws/2/release/{mb_id}?inc=artists&fmt=json').json()
		album_to_edit = Album.objects.get(pk=id)
		album_to_edit.title = mb_lookup['title']
		album_to_edit.artist = Artist.objects.get_or_create(
			name = mb_lookup['artist-credit'][0]['artist']['name'],
			defaults = {
				'mb_id': mb_lookup['artist-credit'][0]['artist']['id']
			}
		)[0]
		album_to_edit.release_date = mb_lookup['date'],
		album_to_edit.mb_id = new_mb_id
		
		album_to_edit.save()

		return {
			"message": "success"
		}
	except Exception:
		return {
			"message": "Internal Server Error"
		}