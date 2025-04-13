# app/main.py
from fastapi import FastAPI
from app.api.endpoints import posts_api, stripe_api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://frontend-977711708959.europe-west1.run.app",
        "https://betterpost.ing",
    ],  # Update for your frontend domain
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(posts_api.router)
app.include_router(stripe_api.router)
