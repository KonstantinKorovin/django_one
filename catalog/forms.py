import re

from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product


CASINO = "казино"
CRIPTO_ONE = "криптовалюта"
CRIPTO_TWO = "крипта"
STOCK = "биржа"
LOW_PRICE = "дешево"
FREE = "бесплатно"
LIE = "обман"
POLICE = "полиция"
RADAR = "радар"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "description", "image", "category", "price")
        exclude = ("created_at", "updated_at", "views_counter")

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите название продукта",
            }
        )
        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите описание продукта",
            }
        )
        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )
        self.fields["category"].widget.attrs.update(
            {
                "class": "form-checkbox",
            }
        )
        self.fields["price"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Укажите цену продукта"
            }
        )

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise ValidationError(
                "Цена не может быть отрицательной или равняться нулю!"
            )
        return price

    def clean(self):
        spam_data = (
            CASINO,
            CRIPTO_ONE,
            CRIPTO_TWO,
            STOCK,
            LOW_PRICE,
            FREE,
            LIE,
            POLICE,
            RADAR,
        )
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        category = cleaned_data.get("category")
        if category is None:
            self.add_error("category", "Укажите категорию продукта.")
        for spam in spam_data:
            if re.findall(spam, name.replace(" ", ""), flags=re.I):
                self.add_error(
                    "name", f"Название продукта не может содержать значение '{spam}'"
                )
            elif re.findall(spam, description.replace(" ", ""), flags=re.I):
                self.add_error(
                    "description",
                    f"Описание продукта не может содержать значение '{spam}'",
                )
