from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class LoginRequiredMixin(AccessMixin):
    """Mixin that verifies that the current user is authenticated.
    Expects the user to be set by custom middleware (`request.corbado_user`).
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.corbado_user:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)