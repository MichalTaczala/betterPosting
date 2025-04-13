# app/api/endpoints/posts.py
import markdown
from fastapi import APIRouter

from app.schemas.posts import CheckoutRequest, RequestModel
from app.services import openai_service, sendgrid_service, tweets_service

router = APIRouter()


@router.get("/activate-backend")
async def activate_backend():
    return {"message": "Backend is activated"}


@router.post("/check-usernames")
async def check_usernames_endpoint(request: RequestModel):
    username1_exists = await tweets_service.check_if_user_exists(request.username1)
    username2_exists = await tweets_service.check_if_user_exists(request.username2)
    return {"valid": username1_exists and username2_exists}


async def handle_success(payload: CheckoutRequest):
    current_user_tweets = await tweets_service.get_tweets(
        payload.current_user, limit=10
    )
    print("⚠️ Current user tweets", flush=True)
    target_user_tweets = await tweets_service.get_tweets(payload.target_user, limit=10)
    print("⚠️ Target user tweets", flush=True)
    i = 0
    while i < 10:
        response = openai_service.analyze_tweets(
            current_user_tweets, target_user_tweets
        )
        i += 1
        if response:
            print("⚠️ Response", flush=True)
            break

    sendgrid_service.send_email(
        payload.email, "Your comparison report", markdown.markdown(response)
    )
    print(
        f"✅ Payment successful for {payload.current_user}, {payload.target_user}, sending to {payload.email}"
    )
