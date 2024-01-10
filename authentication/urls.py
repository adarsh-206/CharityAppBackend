# authentication/urls.py

from django.urls import path
from .views import SignupView, LoginView, TokenCheckView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('check-token/', TokenCheckView.as_view(), name='check-token'),
]
