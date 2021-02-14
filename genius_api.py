import requests
import os
from dotenv import load_dotenv, find_dotenv

# Load and find any vars in env (API keys)
load_dotenv(find_dotenv())

BASE_URL = 'https://api.genius.com'

path = 'search/'

request_uri = '/'.join([BASE_URL, path])

headers = {
    'Authorization': 'Bearer {token}'.format(token=os.getenv('GENIUS_ACCESS_TOKEN'))
    }


def get_lyrics(artist_name, song_name):
    if '(' in song_name:
        song_name = song_name.split('(')
        other_artists = song_name[1].split('feat. ')[1].strip(')')
        song_name = song_name[0]
    params = {'q': artist_name + " " + song_name,
        'text_format': 'dom',
    }
    
    r = requests.get(request_uri, params=params, headers=headers)
    
    r = r.json()
    
    remote_song_info = None
    
    for hit in r['response']['hits']:
        if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
            remote_song_info = hit
            break
    
    if remote_song_info:
        song_url = remote_song_info['result']['url']
        return song_url
    