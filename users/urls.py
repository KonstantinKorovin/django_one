from users.apps import UsersConfig
from django.urls import path

from users.views import UserLoginView, UserLogoutView, UserRegistrationView

app_name = UsersConfig.name


urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(next_page="users:logout"), name="logout"),
    path("register/", UserRegistrationView.as_view(), name="register"),
]
