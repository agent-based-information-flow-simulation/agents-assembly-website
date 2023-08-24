import os

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    client_cors_domain: str = os.environ.get("CLIENT_CORS_DOMAIN", "")
    enable_reload: bool = bool(os.environ.get("RELOAD", False))
    port: int = int(os.environ.get("PORT", 8000))


app_settings = AppSettings()
