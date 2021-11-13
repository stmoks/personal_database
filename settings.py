import os
from decouple import config

SPOTIFY_CID = config('SPOTIFY_CID',default ='702f99bae6f5489da997f6c86663956b')
SPOTIFY_SECRET_ID = config('SPOTIFY_SECRET_ID',default = '08d83f6fe0a0483799fb4891477e757b')
SPOTIFY_REDIRECT_URL = config('SPOTIFY_REDIRECT_URL',default = 'https://www.google.com/')
SPOTIFY_USERNAME = config('SPOTIFY_USERNAME',default = 'j389o9xb4nnxfn1fvoftubvst')
SPOTIFY_SCOPE = config('SPOTIFY_SCOPE',default = 'user-top-read user-read-private user-read-playback-state user-modify-playback-state')

INDEED_CLIENT_ID = config('3314d4331b7cfe4832f76b97c6becb8d05b224efb25304056972d9ca41b8e676')
INDEED_SECRET_ID = config('OwGUYdsvbpjYxgUX5pgisRRTYR83uiRoi560LN9yq32G5X2vBOZa9icMHHn8hB5D')
