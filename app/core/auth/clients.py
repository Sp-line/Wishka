from httpx_oauth.clients.google import GoogleOAuth2

from app.core.config import settings

google_oauth_client = GoogleOAuth2(
    settings.oauth.google.client_id,
    settings.oauth.google.client_secret,
)
