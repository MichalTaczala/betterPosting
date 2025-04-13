import asyncio
from configparser import ConfigParser
from twikit import Client, TooManyRequests


async def main():
    config = ConfigParser()
    config.read("app/core/config.ini")
    print("config", config, flush=True)
    username = config["X"]["username"]
    password = config["X"]["password"]
    email = config["X"]["email"]
    client = Client(language="en-US")
    # await client.login(auth_info_1=username, auth_info_2=email, password=password)
    # client.save_cookies("cookies.json")
    client.load_cookies("cookies.json")

    user_id = "radakanis"
    user = await client.get_user_by_screen_name(user_id)
    user_id = user.id
    tweets = await client.get_user_tweets(user_id, "Tweets", count=10)
    for tweet in tweets:
        print(tweet._data["legacy"]["full_text"])
        # print(vars(tweet))
        break


if __name__ == "__main__":
    asyncio.run(main())
