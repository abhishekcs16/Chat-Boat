import tweepy

consumer_key = 'your consumer_key'

consumer_secret = 'your consumer_secret'

access_token = 'your access_token'

access_token_secret = 'your access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# first tweet
api.update_status(status="This is a sample tweet using Tweepy with python")

# printing user information

user = api.get_user('realDonaldTrump')
print("Name:",user.name)
print("Location:",user.location)
print("Following:",user.friends_count)
print("Followers:",user.followers_count)
