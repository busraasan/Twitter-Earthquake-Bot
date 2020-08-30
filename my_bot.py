import tweepy
import requests
import time
from os import environ

consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_KEY']
access_token_secret = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

response = requests.get('https://api.orhanaydogdu.com.tr/deprem/live.php?limit=1')
data = response.json()
data = [str(data['result'][0]['lokasyon']), str(data['result'][0]['date']), str(data['result'][0]['mag'])]

i = 0
while True:
    time.sleep(10)
    response = requests.get('https://api.orhanaydogdu.com.tr/deprem/live.php?limit=1')
    data2 = response.json()
    data2 = [str(data2['result'][0]['lokasyon']), str(data2['result'][0]['date']), str(data2['result'][0]['mag'])]
    if data[0] != data2[0] or data[1] != data2[1] or data[2] != data[2]:
         api.update_status("Yer: " + data2[0] + "\n" + "Tarih: " + data2[1] + "\n" + 'Şiddet: ' + data2[2])
         data[0] = data2[0]
         data[1] = data2[1]
         data[2] = data2[2]

