from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("phone_number", "is_client", "is_worker")


class PhoneLoginForm(AuthenticationForm):
    username = forms.CharField(label="Phone Number", max_length=15)
