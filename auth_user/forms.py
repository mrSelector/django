from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.NumberInput()

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'phone', 'password1', 'password2')

        def save(self, commit=True):
            user = super().save(commit=False)
            user.email(self.cleaned_data["email"])
            user.phone(self.cleaned_data["phone"])
            if commit:
                user.save()
            return user
