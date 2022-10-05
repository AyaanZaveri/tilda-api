from flask import Flask, request
from ytmusicapi import YTMusic
from flask_cors import CORS

ytmusic = YTMusic()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Invalid Route!'


@app.route('/search/all/<query>', methods=['GET', 'POST'])
def search_get(query):
    search_results = ytmusic.search(query)
    return search_results


@app.route('/search/tracks/<tracks>', methods=['GET', 'POST'])
def tracks_search_get(tracks):
    tracks_search_results = ytmusic.search(tracks, 'songs')
    return tracks_search_results


@app.route('/search/artists/<artists>', methods=['GET', 'POST'])
def artists_search_get(artists):
    artists_search_results = ytmusic.search(artists, 'artists')
    return artists_search_results


@app.route('/search/albums/<albums>', methods=['GET', 'POST'])
def albums_search_get(albums):
    albums_search_results = ytmusic.search(albums, 'albums')
    return albums_search_results


@app.route('/album/<albumId>', methods=['GET', 'POST'])
def album_get(albumId):
    albums_results = ytmusic.get_album(albumId)
    return albums_results


@app.route('/track/<trackId>', methods=['GET', 'POST'])
def track_get(trackId):
    track_results = ytmusic.get_song(trackId)
    return track_results


@app.route('/lyrics/<trackId>', methods=['GET', 'POST'])
def track_lyrics_get(trackId):
    track_lyrics_get = ytmusic.get_lyrics(trackId)
    return track_lyrics_get


@app.route('/artist/<artistId>', methods=['GET', 'POST'])
def artist_get(artistId):
    artist_results = ytmusic.get_artist(artistId)
    return artist_results
  
@app.route('/playlist/<playlistId>', methods=['GET', 'POST'])
def playlist_get(playlistId):
    playlist_results = ytmusic.get_playlist(playlistId)
    return playlist_results
  
@app.route('/albumBrowse/<albumBrowseId>', methods=['GET', 'POST'])
def album_browse_get(albumBrowseId):
    album_browse_results = ytmusic.get_album_browse_id(albumBrowseId)
    return album_browse_results
