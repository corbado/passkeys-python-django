from django.conf import settings


# scs name:
def corbado_settings(request):
    return {
        'CORBADO_PROJECT_ID': settings.CORBADO_PROJECT_ID,
        'CORBADO_FRONTEND_API': settings.CORBADO_FRONTEND_API,
        'CORBADO_BACKEND_API': settings.CORBADO_BACKEND_API,
        'corbado_user': request.corbado_user
    }
