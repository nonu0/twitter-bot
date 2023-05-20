import tweepy
import requests
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
# public_tweet = api.home_timeline()
# for tweet in public_tweet:
#     print(tweet.text)

# Function to download media from a tweet
def download_media(tweet_id, save_path):
    try:
        tweet = api.get_status(tweet_id, tweet_mode="extended")
        media = tweet.entities.get("media", [])
        if len(media) > 0:
            for index, item in enumerate(media):
                media_url = item["media_url"]
                file_extension = media_url.split(".")[-1]
                file_name = f"{save_path}_{index+1}.{file_extension}"
                response = requests.get(media_url)
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"Downloaded media: {file_name}")
        else:
            print("No media found in the tweet.")
    # except tweepy.error.TweepError as e:
    except AttributeError as e:
        print(f"Error occurred: {str(e)}")

# Example usage
tweet_id = "1659605068117688339"  # Replace with the tweet ID you want to download media from
save_path = "C:\\Users\pc\Desktop\twitter"  # Replace with the desired save path
download_media(tweet_id, save_path)
