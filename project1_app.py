import requests
import os
from dotenv import load_dotenv, find_dotenv

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

#header info with access_token ^ used in GET request to the API server
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

