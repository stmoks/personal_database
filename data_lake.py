# streaming data + batch data
# security - hashing + salting of sensitive data
# apis - events, food and drink,geocoding,jobs,music,open data,shopping,social,weather

import pandas as pd
from spotipy import SpotifyClientCredentials,Spotify,util
from datetime import datetime

import spotipy,os
from settings import SPOTIFY_CID,SPOTIFY_SECRET_ID,SPOTIFY_REDIRECT_URL,SPOTIFY_USERNAME,SPOTIFY_SCOPE


# Spotify authentication
client_credentials_manager = SpotifyClientCredentials(client_id = SPOTIFY_CID,client_secret = SPOTIFY_SECRET_ID)

try:
    token = util.prompt_for_user_token(SPOTIFY_USERNAME, SPOTIFY_SCOPE,SPOTIFY_CID,SPOTIFY_SECRET_ID,SPOTIFY_REDIRECT_URL)
except (AttributeError):
    os.remove(f'.cache-{SPOTIFY_USERNAME}')
    token = util.prompt_for_user_token(SPOTIFY_USERNAME, SPOTIFY_SCOPE,SPOTIFY_CID,SPOTIFY_SECRET_ID,SPOTIFY_REDIRECT_URL)

sp = Spotify(client_credentials_manager=client_credentials_manager,auth=token)

# most popular songs of the year - around the world (change market)
artist_name = []
artist_id = []
track_name = []
popularity = []
track_id = []

search_results = sp.search(q = f"year:{(datetime.today().strftime('%Y'))}", type = 'track',market='ZA', limit = 50)

for j,tr in enumerate(search_results['tracks']['items']):
    artist_name.append(tr['artists'][0]['name'])
    track_name.append(tr['name'])
    track_id.append(tr['id'])
    popularity.append(tr['popularity'])

    
track_dataframe = pd.DataFrame({'artist_name':artist_name,'track_name':track_name,'track_id':track_id,'popularity':popularity})


# the most popular tracks
new_df = track_dataframe.sort_values('popularity',ascending=False)
new_df = new_df.drop_duplicates('track_id')
print(new_df.head(10))



#########################################################################################################################################

#todo Do i need to index one of the columns below? Indexes make searching faster
# contact_details = pd.read_excel('contact_details.xlsx',dtype={'cell_number':str},na_values='Missing',names=['first_name','last_name','cell_number','email_address','date_of_birth','occupation','education','gender','location','id_number'])



#########################################################################################################################################
# Indeed job API...