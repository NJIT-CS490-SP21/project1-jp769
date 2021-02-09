import os

from flask import Flask, render_template
from spotify_api import get_data

app = Flask(__name__)

# copied from lect6, read doc on max age
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    print('\nRan, updated.\n')
    
    spotify_data = get_data()
    print(spotify_data['main_song']['song_name'])
    print(spotify_data['main_song']['song_image'])
    print(spotify_data['other_songs']['song_names'])
    print(spotify_data['other_songs']['song_image'])
    # print(spotify_data['json_r'])

    return render_template(
        "index.html",
        song_image = spotify_data['main_song']['song_image'],
        song_name = spotify_data['main_song']['song_name'],
        other_songs = spotify_data['other_songs']['song_names'],
        other_songs = spotify_data['other_songs']['song_image'],
        num_songs = len(spotify_data['other_songs']['song_names'])
    #     artist = spotify_data['main_artist'],
    #     num_artists = spotify_data['num_artists'],
    #     all_artists = spotify_data['all_artists'],
    #     song_preview = spotify_data['song_preview'],
    )

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
