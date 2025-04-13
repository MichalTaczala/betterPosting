from typing import List

from openai import OpenAI

from app.core.config import get_settings

settings = get_settings()


def analyze_tweets(my_tweets: List[str], my_idol_tweets: List[str]):
    client = OpenAI(api_key=settings.openai_api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that help users write better tweets, that have the similar style to other users tweets",
            },
            {
                "role": "user",
                "content": "First, I will give you my tweets as a list",
            },
            {
                "role": "user",
                "content": f"{my_tweets}",
            },
            {
                "role": "user",
                "content": "Now i will give you my idol tweets as a list",
            },
            {
                "role": "user",
                "content": f"{my_idol_tweets}",
            },
            {
                "role": "user",
                "content": "Your job is to analyze my tweets and my idol tweets and write me a report about my tweets, and give me some advice about how to improve my tweets. Pay attention to the style of my idols tweets and give me some techniques and improvements that he uses in his tweets and I don't.",
            },
        ],
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content
