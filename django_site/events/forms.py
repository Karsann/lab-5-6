from django import forms
from django.core.exceptions import ValidationError


class EventRegistrationForm(forms.Form):
    name = forms.CharField(
        label="Ваше ім'я",
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder": "Введіть ім'я"})
    )
    email = forms.EmailField(
        label="Електронна пошта",
        widget=forms.EmailInput(attrs={"placeholder": "example@mail.com"})
    )
    event = forms.ChoiceField(
        label="Оберіть подію",
        choices=[
            ("python", "Python Meetup"),
            ("ai", "AI Conference"),
            ("frontend", "Frontend Workshop")
        ]
    )
    comment = forms.CharField(
        label="Побажання / Коментар",
        required=False,
        max_length=200,
        widget=forms.Textarea(attrs={"rows": 4})
    )

    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        if any(char.isdigit() for char in name):
            raise ValidationError("Ім'я не повинно містити цифр")
        if len(name) < 2:
            raise ValidationError("Ім'я має містити щонайменше 2 символи")
        return name