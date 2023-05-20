import tweepy
import requests

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

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
    except tweepy.TweepError as e:
        print(f"Error occurred: {str(e)}")

# Example usage
tweet_id = "123456789"  # Replace with the tweet ID you want to download media from
save_path = "path/to/save/media"  # Replace with the desired save path
download_media(tweet_id, save_path)
