
# PabloAndDaisyBot

import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('Pups')

# iterates over pictures in models folder
for pup_image in os.listdir('.'):
    api.update_with_media(pup_image)
    time.sleep(86400)
