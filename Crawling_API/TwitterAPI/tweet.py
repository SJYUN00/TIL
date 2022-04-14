import json
import tweepy
from google.cloud import pubsub_v1
from google.oauth2 import service_account

key_path = "twitterapi-347207-de899f32fd72.json"
credentials = service_account.Credentials.from_service_account_file(
 key_path,
 scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
client = pubsub_v1.PublisherClient(credentials=credentials)
topic_path = client.topic_path('twitterapi', 'tweets')


twitter_api_key = 'JZf9Rg3mZVxt2A37ZdWcswmFf'
twitter_api_secret_key = 'rEMQKE9NUcSCVyHNRXeECth2yuDM1yfZwcNreKEKz4204eh5jf'
twitter_access_token = '1513914895905210369-AljCvRuBPk8ZiwlLFueCEbJ6hgF3GN'
twitter_access_token_secret = 'vQXRJ71uyZNuk5gLPMsJds1uIbiEyHJUkRPE2jY2B5WCZ'

class SimpleStreamListener(tweepy.StreamListener):
 def on_status(self, status):
    print(status)
    tweet = json.dumps({'id': status.id, 'created_at': status.created_at, 'text': status.text}, default=str)
    client.publish(topic_path, data=tweet.encode('utf-8'))

 def on_error(self, status_code):
    print(status_code)
    if status_code == 420:
        return False

stream_listener = SimpleStreamListener()
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret_key)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)
twitterStream = tweepy.Stream(auth, stream_listener)
twitterStream.filter(track=['data'])

# import tweepy

# twitter_api_key = 'JZf9Rg3mZVxt2A37ZdWcswmFf'
# twitter_api_secret_key = 'rEMQKE9NUcSCVyHNRXeECth2yuDM1yfZwcNreKEKz4204eh5jf'
# twitter_access_token = '1513914895905210369-AljCvRuBPk8ZiwlLFueCEbJ6hgF3GN'
# twitter_access_token_secret = 'vQXRJ71uyZNuk5gLPMsJds1uIbiEyHJUkRPE2jY2B5WCZ'

# # StreamListener 를 상속 받는 클래스 생성
# # 그 클래스를 이용해 Stream 객체를 생성
# class SimpleStreamListener(tweepy.StreamListener):
#  def on_status(self, status):
#   print(status.text)

# stream_listener = SimpleStreamListener()
# auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret_key)
# auth.set_access_token(twitter_access_token, twitter_access_token_secret)
# twitterStream = tweepy.Stream(auth, stream_listener) # Stream 을 사용해서 트위터 API에 연결
# twitterStream.filter(track=['pokemon'])