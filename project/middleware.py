from .utils.authentication import get_authenticated_user_from_cookie, get_authenticated_user_from_authorization_header
from dataclasses import dataclass
from django.utils.deprecation import MiddlewareMixin

@dataclass(frozen=True)
class CorbadoUser:
    user_id: str
    full_name: str


class CorbadoAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.corbado_user = None
        validation_result = get_authenticated_user_from_cookie(request)
        if not validation_result:
            validation_result = get_authenticated_user_from_authorization_header(request)
        if validation_result:
            request.corbado_user = CorbadoUser(user_id=validation_result.user_id, full_name=validation_result.full_name)