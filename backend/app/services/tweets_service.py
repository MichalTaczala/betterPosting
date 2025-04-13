from configparser import ConfigParser

import httpx
from twikit import Client

TWEETS = 10


async def get_tweets(username: str, limit: int = 20):
    config = ConfigParser()
    config.read("app/core/config.ini")
    my_personal_username = config["X"]["username"]
    password = config["X"]["password"]
    email = config["X"]["email"]
    client = Client(language="en-US")

    try:
        client.load_cookies("cookies.json")
    except Exception:
        client.login(
            auth_info_1=my_personal_username, auth_info_2=email, password=password
        )
        client.save_cookies("cookies.json")

    user = await client.get_user_by_screen_name(username)
    user_id = user.id
    tweets_text = []
    tweets_whole = await client.get_user_tweets(user_id, "Tweets", count=limit)
    for tweet in tweets_whole:
        tweets_text.append(tweet._data["legacy"]["full_text"])
    return tweets_text


async def check_if_user_exists(username):
    url = f"https://x.com/{username}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
    }

    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(url, headers=headers)
    print(response.status_code)

    if response.status_code == 200:
        return True
    else:
        return False
