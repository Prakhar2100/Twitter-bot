#Implemented by - PRAKHAR KOCHAR
#Libraries downloaded - tweepy (suitable for python version)
#Python Version Used- 3.8.2

import tweepy
import time

CONSUMER_KEY = '#'
CONSUMER_SECRET = '#'
ACCESS_KEY = '#'
ACCESS_SECRET = '#'

#OAuthHandler to get access to twitter developer app data
auth = tweepy.OAuthHandler(CONSUMER_KEY , CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

#Creating a file and reading last seen id of the message sent
def retrieve_last_seen_id(file_name):
    f_read = open(file_name , 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id
#Storing the last seen id from the file created to ensure one retweet to every tweet
def store_last_seen_id(last_seen_id , file_name):

    f_write = open(file_name , 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

#Checking the validity of tweet sent and replying accordingly
def ready_to_retweet():
    print('replying to incoming tweet...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')
    #Idea of replying to tweets is Queue data structure (FIFO)
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if 'hi' in mention.full_text.lower():
            print('found hi!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name + ' Hello Dear!' , mention.id)

while True:
    ready_to_retweet()
    time.sleep(15)

