# project1-jp769 Spotify API and Flask (Web app)

## REQUIREMENTS:
1. `pip install Flask`
2. `pip install python-dotenv`
3. `pip install requests`
(Note, if pip install does not work try: sudo pip install or use pip3 instead of pip)

## Setup
1. Create `.env` file in your project directory
2. Add your SpotifyAPI Client ID and Client Secret from your application dashboard (https://developer.spotify.com/dashboard/applications) with the lines: 
    `export CLIENT_ID='YOUR_CLIENT_ID'`
    `export CLIENT_ID='YOUR_CLIENT_SECRET'`
3. In `spotify_api.py`, you can change the list in Line 16 to contain your favorite artists id: `favorite_artists_id = ['artist1_id', 'artist2_id', 'etc']`. See [How to Find Artist ID](https://support.tunecore.com/hc/en-us/articles/360040325651-How-to-Find-my-Spotify-Artist-ID).


## Run Application
1. Run command in terminal `python project1_app.py`
2. Preview web page in browser '/'