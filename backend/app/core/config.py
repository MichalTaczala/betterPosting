from functools import cache
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env: str
    stripe_price_id: str
    stripe_webhook_secret: str
    stripe_secret_key: str
    openai_api_key: str
    sendgrid_api_key: str
    frontend_url: str
    debug: bool

    class Config:
        env_file = f'.env.{os.getenv("ENV", "dev")}'


@cache
def get_settings() -> Settings:
    return Settings()
