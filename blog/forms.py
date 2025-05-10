from django import forms
from blog.models import BlogModel


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ("header", "description", "preview", "created_at", "is_publication")

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        self.fields["header"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите название статьи",
            }
        )
        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите текст",
            }
        )
        self.fields["preview"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )
        self.fields["created_at"].widget.attrs.update(
            {
                "class": "form-checkbox",
            }
        )
        self.fields["is_publication"].widget.attrs.update(
            {
                "class": "form-checkbox",
            }
        )
