from django.conf import settings


# scs name:
def corbado_settings(request):
    return {
        'CORBADO_PROJECT_ID': settings.CORBADO_PROJECT_ID,
        'CORBADO_TELEMETRY_DISABLED': str(settings.CORBADO_TELEMETRY_DISABLED == 'true').lower(),
        'CORBADO_FRONTEND_API': settings.CORBADO_FRONTEND_API,
        'corbado_user': request.corbado_user
    }
