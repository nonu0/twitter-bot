import tweepy

api_key = 'Jg4Ks1W4ZsbIB5iZu9hXhoPGG'
api_secret = '2TiOk9F7Ey5Z8JuI9YcdMGf8Dv8hs8amfx896hJm6aUtIChasx'
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAJ3%2FnQEAAAAAsrSJjjj2uFeiZd3wRBzAI%2FSJ9yc%3DSitVgZKoAj0gBFaM5aMwP6jl7YBBpowQbFpI3RRlP6qerpPwID"
access_token = '1653373313064792065-TizIjIvw66l7GmqONi9UO6pbJ4kJLS'
access_token_secret = "J2QyPmoXnHbRBmf6cVF0LQISKuSYw4TZzq9yFuhO08WDY"
client_id = 'ZXR2WnVaYThvTWE1TkRKcl9hY0o6MTpjaQ'
client_secret = 'V5C8bSnxLJcdjeoAsaztfsmz8E4X3COUIyec0T7OqtHZ4abW-Q'

client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key,api_secret,access_token,access_token_secret)
api = tweepy.API(auth)

# client.create_tweet(text = 'hello')
public_tweet = api.home_timeline()
for tweet in public_tweet:
    print(tweet.text)
