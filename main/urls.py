from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('signup/onboarding/', Onboarding.as_view(), name='onboarding'),
    path('login/', Login.as_view(), name='login'),
    path('profile/', Profile.as_view(), name='profile'),
    path('userarea/', UserArea.as_view(), name='user_area'),
    path('api/secret/', secret_view, name='secret_view'),
]