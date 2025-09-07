from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm


class UserLoginView(LoginView):
    template_name = "registration/login.html"


class UserLogoutView(LogoutView):
    template_name = "registration/logout.html"


class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"

    def get_success_url(self):
        return reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    @staticmethod
    def send_welcome_email(user_email):
        subject = "Добро пожаловать в наш сервис!"
        message = "Спасибо за регистрацию!"
        from_email = "rackitinkon@yandex.ru"
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)
