import requests
import os
from dotenv import load_dotenv, find_dotenv
import random

# Load and find any vars in env (API keys)
load_dotenv(find_dotenv())

# URL to send request for app authorization (get access token)
AUTH_URL = 'https://accounts.spotify.com/api/token'

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# hardcoded Spotify artists ids 
favorite_artists_id = [
    '0fA0VVWsXO9YnASrzqfmYu',
    '4MCBfE4596Uoi2O4DtmEMz',
    '5INjqkS1o8h1imAzPqGZBb',
    '4q3ewBCX7sLwd24euuV69X',
    '2h93pZq0e7k5yf4dywlkpM',
    '4O15NlyKLIASxsJ0PrXPfz',
    '1RyvyyTE3xzB2ZywiAwp0i',
    '1tq9rmv85VHcxqvNdO1DQP'
]

def get_data():
    # POST from https://stmorse.github.io/journal/spotify-api.html to get access token
    response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
    })
    
    response_data = response.json()
    
    # parsing/accessing only the access_token from response
    access_token = response_data['access_token']
    
    # print(access_token) #TESTING PURPOSES ONLY!! Needed if trying spotify api on web console
    
    #header info with access_token ^ used in GET request to the API server
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    
    # Randomly choosing an artist from list
    random_artist = random.randint(0, len(favorite_artists_id)-1)
    
    market='?market=US'
    
    # Fetching top tracks of artist
    r = requests.get(BASE_URL + 'artists/{id}/top-tracks'.format(id=favorite_artists_id[random_artist]) + market, headers=headers)
    
    # 
    r = r.json()
    
    # Randomly choosing a song from the given top tracks
    random_song = random.randint(0, len(r['tracks'])-1)
    
    # Information of main song (randomly choosen) stored in dictionary
    main = {
        'song_name': r['tracks'][random_song]['name'],
        'song_image': r['tracks'][random_song]['album']['images'][1]['url'],
        'song_preview': r['tracks'][random_song]['preview_url'],
        'num_artists': len(r['tracks'][random_song]['artists']),
        'main_artist': '',
        'artists': []
    }
    
    # Dictionary holding the other top tracks of artist (list of the names and images)
    other_tracks={
        'song_names': [],
        'song_image': []
    }
    
    # Population artist(s) and main artist data in main dictionary
    for i in range (0,main['num_artists']):
        if(r['tracks'][random_song]['artists'][i]['id'] == favorite_artists_id[random_artist]):
            main['main_artist'] = r['tracks'][random_song]['artists'][i]['name']
        main['artists'].append(r['tracks'][random_song]['artists'][i]['name'])
    
    #Population other tracks with name and image to display
    for i in range (0,len(r['tracks'])):
        if(i != random_song):
            other_tracks['song_names'].append(r['tracks'][i]['name'])
            other_tracks['song_image'].append(r['tracks'][i]['album']['images'][2]['url'])

    return {
        'main_song': main,
        'other_songs': other_tracks
    }