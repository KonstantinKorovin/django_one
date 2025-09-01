from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        help_text="Необязательное поле. Введите ваш номер телефона.",
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", "phone_number", "avatar", "country")

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите свой e-mail адрес."}
        )

        self.fields["phone_number"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите свой номер телефона."}
        )

        self.fields["avatar"].widget.attrs.update({"class": "checkbox"})

        self.fields["country"].widget.attrs.update({"class": "form-control"})


class CustomUserAuthenticationForm(AuthenticationForm):
    pass
