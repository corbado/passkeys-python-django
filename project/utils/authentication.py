from corbado_python_sdk.generated.models import IdentifierList
from django.conf import settings
from django.http import HttpRequest
from corbado_python_sdk import Config, CorbadoSDK, UserEntity

config = Config(
    project_id=settings.CORBADO_PROJECT_ID,
    api_secret=settings.CORBADO_API_SECRET,
    frontend_api=settings.CORBADO_FRONTEND_API,
    backend_api=settings.CORBADO_BACKEND_API
)
sdk = CorbadoSDK(config=config)


def get_authenticated_user_from_cookie(req: HttpRequest) -> UserEntity | None:
    session_token = req.COOKIES.get('cbo_session_token')
    if not session_token:
        return None
    try:
        return sdk.sessions.validate_token(session_token)
    except:
        # use more sophisticated error handling in production
        return None


def get_authenticated_user_from_authorization_header(req: HttpRequest) -> UserEntity | None:
    session_token = req.headers.get('Authorization')
    if not session_token:
        return None
    try:
        return sdk.sessions.validate_token(session_token)
    except:
        # use more sophisticated error handling in production
        return None



def get_user_identifiers(user_id: str) -> IdentifierList:
    return sdk.identifiers.list_identifiers(user_id=user_id)
