# project1-jp769 Application

Clone this repo
1. On https://github.com/new, create a new repository. (Name should not matter, but will be needed for step 4!)
2. In Cloud9 terminal, in your home directory, clone the repo:`git clone https://github.com/NJIT-CS490-SP21/project1-jp769.git`
3. cd into the repository that is created and you should see all the files.
4. Then, connect this cloned repo to your new personal repo made in Step 1: git remote set-url origin https://www.github.com/{your-username}/{repo-name} (be sure to change your-username and repo-name, then remove the curly braces)
5. Run git push origin main to push the local repo to remote. You should now see this same code in your personal repo.

## Requirements:
1. `pip install Flask`
2. `pip install python-dotenv`
3. `pip install requests`
(Note, if pip install does not work try: sudo pip install or use pip3 instead of pip)

## Sign up for Spotify Developer Account
1. To use the Web API, start by creating a Spotify user account (Premium or Free). To do that, simply sign up at [Spotify](www.spotify.com).
2. When you have a user account, go to the [Dashboard](https://developer.spotify.com/dashboard) page at the Spotify Developer website and, if necessary, log in. Accept the latest Developer Terms of Service to complete your account set up.

## Sign up for Genius API
1. To use the Genius API, start by signing up for a Genius account. [Genius Signup](https://genius.com/signup_or_login)
2. Go to [Genius Developers](https://genius.com/developers) to create a new API Client

## Setup
1. Create `.env` file in your project directory
2. Add your SpotifyAPI Client ID and Client Secret from your application [dashboard](https://developer.spotify.com/dashboard/applications) with the lines: 
    `export CLIENT_ID='YOUR_CLIENT_ID'`
    `export CLIENT_SECRET='YOUR_CLIENT_SECRET'`
3. Add your Genius API Client Access Token from your API Client [page](https://genius.com/api-clients) with the line:
    `export GENIUS_ACCESS_TOKEN='YOUR_CLIENT_SECRET'`
    (Note, you will have change this if you continuously click to generate new access token)
4. In `spotify_api.py`, you can change the list in Line 16-25 to contain your favorite artists ID: `favorite_artists_id = ['artist1_id', 'artist2_id', 'etc']`. For artist ID see [How to Find Artist ID](https://support.tunecore.com/hc/en-us/articles/360040325651-How-to-Find-my-Spotify-Artist-ID).


## Run Application
1. Run command in terminal `python project1_app.py`
2. Preview web page in browser '/'

## Heroku Deployment
1. Install Heroku CLI: `npm install -g heroku`.
2. Create a free account on [Heroku](https://signup.heroku.com/login) if you do not have an account already
3. Add + commit all changed files with git
4. Log in to Heroku: `heroku login -i`
5. Create a Heroku app: `heroku create`. This will create a new URL and associated host for you.
6. Push your code to Heroku: `git push heroku main`. This actually pushes your code to Heroku's remote repository.
7. Go to your Heroku [dashboard](https://dashboard.heroku.com/apps) and click your App, then go to Settings, and click "Reveal Config Vars"
8. Add your secret key from .env with the matching variable names (CLIENT_ID, CLIENT_SECRET, GENIUS_ACCESS_TOKEN) and value (your key, without quotation marks!)
9. Open your app with your new URL: `heroku open`. Click the link to open if it doesn't open on its own. Voila!


My Heroku Deployment URL: https://protected-headland-54233.herokuapp.com/

### Technical Issues
1. Unable to access my instance/workspace. I started by searching the internet for the error `"This is taking longer than expected. The delay may be caused by high CPU usage in your environment, or your T2 or T3 instance is running out of burstable CPU capacity credits, or there are VPC configuration issues. Please check documentation"`
After reading stackoverflow and other websites I tried to manually stop my instance which was unsuccessful. Afterwards, I looked at the VPC configuration settings and saw that most of the suggestions were already set so that is when I reached out to the professor for help as well as for an extension given the first milestone was due that night.
I ended up having to create a new instance/environment in which I cloned my work that I had saved on my remote repository and worked from there.
2. Genius API authentication gave me some troubles as it was not the same as Spotify or other APIs. I searched for any tutorials or guides to help with the Genius API authentication with no luck as most used libraries for this. Unaware if we could use said libraries I played it safe and instead used a more risky authentication of using the access token stored in locally.
It is not recommended because it does not use the Client ID or Client Secret to check the user is actually the user. In my case it worked out and in the future it would be better to use other libraries, if allowed, that are made specifcally for this issue.
3. Issues deploying the application to both Heroku and regular Flask. It was due to lyrics_url being empty which was easily fixed a try except block before passing the variable to the template. If it was empty or not set then it would set it to None which would be accepted in the if statement in the index.html to display the unavailble error.

### Known Problems
1. Extended songs or remixes do not always have their own lyrics. Searching for lyrics using the song name and artist does not always yield a url to see the lyrics. A fix for this would be to find another search query. It would first search the artist, or artists, and then song name which would be checked for "remix" or "extended version" in the string.
Another way around this would be to use a differnt API to find the lyrics.
3. Not all songs having a preview available is something that could be fixed using other resources, but given that Spotify does not provided them due to copyright issues it is probably best left as is.
