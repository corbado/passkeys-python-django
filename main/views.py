from django.shortcuts import render, redirect
from django.views import View
from .models import User
from .decorators import api_login_required
from .mixins import LoginRequiredMixin
from django.http import JsonResponse
from project.utils.authentication import get_user_identifiers


# Create your views here.

class Home(View):
    def get(self, request):
        if request.corbado_user:
            user = User.objects.get(corbado_user_id=request.corbado_user.user_id)
            return render(
                request, 'main/home_authenticated.html',
                {'city': user.city}
            )
        return render(request, 'main/home_guest.html')


class Signup(View):
    def get(self, request):
        if request.corbado_user:
            return redirect('profile')
        return render(request, 'main/signup.html')


class Onboarding(LoginRequiredMixin, View):
    def get(self, request):
        user, _ = User.objects.get_or_create(corbado_user_id=request.corbado_user.user_id)
        if user.city is not None:
            return redirect('profile')
        return render(request, 'main/onboarding.html')

    def post(self, request):
        user = User.objects.get(corbado_user_id=request.corbado_user.user_id)
        user.city = request.POST['city']
        user.save()
        return redirect('home')


class Login(View):
    def get(self, request):
        if request.corbado_user:
            return redirect('profile')
        return render(request, 'main/login.html')


class UserArea(View):
    def get(self, request):
        if request.corbado_user:
            return render(request, 'main/userarea_authenticated.html')
        return render(request, 'main/userarea_guest.html')


class Profile(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(corbado_user_id=request.corbado_user.user_id)
        identifiers = get_user_identifiers(request.corbado_user.user_id)
        return render(
            request, 'main/profile.html',
            {'example_id': user.id, 'corbado_id': user.corbado_user_id, 'identifiers': identifiers.identifiers}
        )

@api_login_required
def secret_view(request):
    return JsonResponse({'secret': 'Passkeys are cool!'})