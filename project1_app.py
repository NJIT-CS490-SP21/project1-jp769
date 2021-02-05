import requests
import os
from dotenv import load_dotenv, find_dotenv
import random

# URL to send request for app authorization (get access token)
AUTH_URL = 'https://accounts.spotify.com/api/token'

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# Load and find any vars in env
load_dotenv(find_dotenv())

# POST from https://stmorse.github.io/journal/spotify-api.html to get access token
response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': os.getenv('CLIENT_ID'),
    'client_secret': os.getenv('CLIENT_SECRET'),
})

response_data = response.json()

# parsing/accessing only the access_token from response
access_token = response_data['access_token']

# print(access_token)

#header info with access_token ^ used in GET request to the API server
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

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

random_number = random.randint(0, len(favorite_artists_id)-1)
# print(len(favorite_artists_id), random_number)
print(favorite_artists_id[random_number])

market='?market=US'

# Fetching top tracks of artist
r = requests.get(BASE_URL + 'artists/{id}/top-tracks'.format(id=favorite_artists_id[random_number]) + market, headers=headers)

r = r.json()

random_number = random.randint(0, len(r['tracks']))

print(len(r['tracks']), random_number)

print(r['tracks'][random_number]['album']['artists'][0]['name'])
print(r['tracks'][random_number]['name'])