from django.urls import path
from .views import login, UserSignupAPIView

urlpatterns = [
    path('signup/', UserSignupAPIView.as_view(), name='user-signup'),
    path('login/', login, name='login'),
]
