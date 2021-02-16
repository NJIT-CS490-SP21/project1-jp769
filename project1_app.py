import os

from flask import Flask, render_template
from spotify_api import get_data
from genius_api import get_lyrics

app = Flask(__name__)

# copied from lect6, read doc on max age
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    print('\nRan, updated.\n')
    
    spotify_data = get_data()
    # print(spotify_data['main_song']['main_artist'], spotify_data['main_song']['song_name'])
    lyrics_url = get_lyrics(spotify_data['main_song']['main_artist'], spotify_data['main_song']['song_name'])
    print(lyrics_url)
    
    return render_template(
        "index.html",
        lyrics_url = lyrics_url,
        song_image = spotify_data['main_song']['song_image'],
        song_name = spotify_data['main_song']['song_name'],
        artist = spotify_data['main_song']['main_artist'],
        num_artists = spotify_data['main_song']['num_artists'],
        all_artists = spotify_data['main_song']['artists'],
        song_preview = spotify_data['main_song']['song_preview'],
        other_songs_names = spotify_data['other_songs']['song_names'],
        other_songs_images = spotify_data['other_songs']['song_image'],
        num_songs = len(spotify_data['other_songs']['song_names']),
    )

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
