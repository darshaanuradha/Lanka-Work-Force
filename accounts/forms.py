from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
import re


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("full_name", "phone_number", "active_role")

        labels = {
            "phone_number": "දුරකථන අංකය",
            "active_role": "රැකියා වර්ගය",
            "full_name": "සම්පූර්ණ නම",
        }

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter password"}),
        help_text="Minimum 8 characters",
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Repeat password"}),
        help_text="Enter the same password again",
    )

    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number")

        # Sri Lanka formats: 0771234567 or +94771234567
        pattern = r"^(?:\+94|0)?7\d{8}$"

        if not re.match(pattern, phone):
            raise forms.ValidationError("වලංගු දුරකථන අංකයක් ඇතුලත් කරන්න (e.g. 0771234567)")

        return phone


class PhoneLoginForm(AuthenticationForm):
    username = forms.CharField(label="Phone Number", max_length=15)
