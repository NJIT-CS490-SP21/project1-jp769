# project1-jp769 Spotify API and Flask (Web app)

## REQUIREMENTS:
1. `pip install Flask`
2. `pip install python-dotenv`
3. `pip install requests`
(Note, if pip install does not work try: sudo pip install or use pip3 instead of pip)

## Sign up for Spotify Developer Account
1. To use the Web API, start by creating a Spotify user account (Premium or Free). To do that, simply sign up at [Spotify](www.spotify.com).
2. When you have a user account, go to the [Dashboard](https://developer.spotify.com/dashboard) page at the Spotify Developer website and, if necessary, log in. Accept the latest Developer Terms of Service to complete your account set up.

## Setup
1. Create `.env` file in your project directory
2. Add your SpotifyAPI Client ID and Client Secret from your application [dashboard](https://developer.spotify.com/dashboard/applications) with the lines: 
    `export CLIENT_ID='YOUR_CLIENT_ID'`
    `export CLIENT_SECRET='YOUR_CLIENT_SECRET'`
3. In `spotify_api.py`, you can change the list in Line 16-25 to contain your favorite artists ID: `favorite_artists_id = ['artist1_id', 'artist2_id', 'etc']`. For artist ID see [How to Find Artist ID](https://support.tunecore.com/hc/en-us/articles/360040325651-How-to-Find-my-Spotify-Artist-ID).


## Run Application
1. Run command in terminal `python project1_app.py`
2. Preview web page in browser '/'
