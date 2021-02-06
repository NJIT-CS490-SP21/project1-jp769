import os

from flask import Flask, render_template
from spotify_api import get_data

app = Flask(__name__)

# copied from lect6, read doc on max age
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    """ Returns root endpoint HTML """
    print('Ran, updated.\n')
    
    spotify_data = get_data()
    
    # print(spotify_data['json_r'])
    print(spotify_data['num_artists'])
    print(spotify_data['main_artist'])
    print(spotify_data['song_name'])
    print(spotify_data['all_artists'])

    return render_template(
        "index.html",
    )

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
