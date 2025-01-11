from corbado_python_sdk.generated.models import IdentifierList
from django.conf import settings
from django.http import HttpRequest
from corbado_python_sdk import Config, CorbadoSDK, SessionValidationResult

config = Config(
    project_id=settings.CORBADO_PROJECT_ID,
    api_secret=settings.CORBADO_API_SECRET,
    _frontend_api=settings.CORBADO_FRONTEND_API,
    backend_api=settings.CORBADO_BACKEND_API
)
sdk = CorbadoSDK(config=config)


def get_authenticated_user_from_cookie(req: HttpRequest) -> SessionValidationResult | None:
    session_token = req.COOKIES.get('cbo_session_token')
    if not session_token:
        return None
    return sdk.sessions.get_and_validate_short_session_value(session_token)


def get_authenticated_user_from_authorization_header(req: HttpRequest) -> SessionValidationResult | None:
    session_token = req.headers.get('Authorization')
    if not session_token:
        return None
    session_token = session_token.replace('Bearer ', '')
    return sdk.sessions.get_and_validate_short_session_value(session_token)



def get_user_identifiers(user_id: str) -> IdentifierList:
    return sdk.identifiers.list_identifiers(user_id=user_id)
