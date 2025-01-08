from django.http import JsonResponse
from functools import wraps

def api_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.corbado_user:
            return view_func(request, *args, **kwargs)
        return JsonResponse({'detail': 'Unauthorized'}, status=401)
    return _wrapped_view