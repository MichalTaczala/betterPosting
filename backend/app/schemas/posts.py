# app/schemas/posts.py
from pydantic import BaseModel


class RequestModel(BaseModel):
    username1: str
    username2: str


class OurPostRequest(BaseModel):
    username: str
    our_post: str


class ChangedPost(BaseModel):
    changed_post: str


class CheckoutRequest(BaseModel):
    email: str
    current_user: str
    target_user: str
