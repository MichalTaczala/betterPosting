import stripe
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from app.api.endpoints.posts_api import handle_success
from app.core.config import get_settings
from app.schemas.posts import CheckoutRequest

settings = get_settings()

router = APIRouter()


stripe.api_key = settings.stripe_secret_key
WEBHOOK_SECRET = settings.stripe_webhook_secret


@router.post("/create-checkout-session")
async def create_checkout_session(data: CheckoutRequest):
    session = stripe.checkout.Session.create(
        line_items=[
            {
                "price": settings.stripe_price_id,
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=f"{settings.frontend_url}/success",
        cancel_url=f"{settings.frontend_url}/cancel",
        automatic_tax={"enabled": True},
        customer_email=data.email,
        metadata={
            "current_user": data.current_user,
            "target_user": data.target_user,
        },
    )
    return {"id": session.id}


@router.post("/webhook")
async def stripe_webhook(request: Request):
    print("⚠️ Stripe webhook received", flush=True)
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, WEBHOOK_SECRET)
    except ValueError as e:
        print("⚠️ Invalid payload", e)
        return JSONResponse(status_code=400, content={"error": "Invalid payload"})
    except stripe.error.SignatureVerificationError as e:
        print("⚠️ Invalid signature", e)
        return JSONResponse(status_code=400, content={"error": "Invalid signature"})

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        current_user = session["metadata"]["current_user"]
        target_user = session["metadata"]["target_user"]
        email = session["customer_email"]

        print(
            f"✅ Payment successful for {current_user}, {target_user}, sending to {email}"
        )

        # Call your async logic to generate result & send email
        print("⚠️ Calling handle_success", flush=True)
        await handle_success(
            CheckoutRequest(
                email=email, current_user=current_user, target_user=target_user
            )
        )

    return JSONResponse(status_code=200, content={"message": "Webhook received."})
