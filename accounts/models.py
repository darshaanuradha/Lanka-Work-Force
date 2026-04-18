from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number must be set")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)  # Hashes the standard password
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom authentication user model that uses ``phone_number`` as the unique login identifier
    instead of username/email.
    Why these fields are here:
    - ``full_name``: stores the user's display/name value.
    - ``phone_number``: primary credential for authentication (``USERNAME_FIELD``) and must be unique.
    - ``active_role``: tracks the currently selected app role (``Client`` or ``Worker``).
    - ``is_active``: controls whether the account is enabled for login.
    - ``is_staff``: grants access to Django admin/staff-only areas.
    - ``date_joined``: records account creation timestamp.
    - ``objects``: custom manager required for creating users/superusers correctly with this model.
    Auth configuration:
    - ``USERNAME_FIELD = "phone_number"`` tells Django to authenticate with phone numbers.
    - ``REQUIRED_FIELDS = []`` is intentional because with this setup only phone number and password
        are required by default when creating a superuser.
    """

    full_name = models.CharField(max_length=255, default="john doe")
    phone_number = models.CharField(max_length=15, unique=True)
    ROLE_CHOICES = [
        ("Client", "Client"),
        ("Worker", "Worker"),
    ]
    active_role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default="Client"
    )

    # Required fields for Django admin and permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    # REQUIRED_FIELDS is empty because phone_number and password are automatically required
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number
