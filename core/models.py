from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name_en = models.CharField(max_length=100, verbose_name="Name (English)")
    name_si = models.CharField(max_length=100, verbose_name="Name (Sinhala)")
    icon_tag = models.CharField(
        max_length=50,
        blank=True,
        help_text="CSS class for the icon (e.g., 'fas fa-hammer')",
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name_en} / {self.name_si}"


class WorkerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="worker_profile",
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="workers"
    )
    LOCATION_CHOICES = [
        ("Kandy", "Kandy"),
        ("Colombo", "Colombo"),
        ("Galle", "Galle"),
        ("Jaffna", "Jaffna"),
        ("Anuradhapura", "Anuradhapura"),
        ("Trincomalee", "Trincomalee"),
        ("Matara", "Matara"),
        ("Hambantota", "Hambantota"),
        ("Nuwara Eliya", "Nuwara Eliya"),
        ("Badulla", "Badulla"),
        ("Ratnapura", "Ratnapura"),
        ("Puttalam", "Puttalam"),
        ("Kurunegala", "Kurunegala"),
        ("Monaragala", "Monaragala"),
        ("Vavuniya", "Vavuniya"),
        ("Mannar", "Mannar"),
        ("Kilinochchi", "Kilinochchi"),
        ("Mullaitivu", "Mullaitivu"),
    ]
    location = models.CharField(
        max_length=255, choices=LOCATION_CHOICES, help_text="Primary location of work"
    )
    daily_rate = models.DecimalField(
        max_digits=8, decimal_places=2, help_text="Daily wage in LKR"
    )
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    is_online = models.BooleanField(
        default=True, help_text="Toggle to show/hide in client searches"
    )

    def __str__(self):
        return f"Worker: {self.user.phone_number} - {self.category.name_en if self.category else 'Uncategorized'}"


class QuickTapTag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    worker = models.ForeignKey(
        WorkerProfile, on_delete=models.CASCADE, related_name="reviews"
    )
    client_name = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews_given"
    )
    star_rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    quicktap_tags = models.ManyToManyField(
        QuickTapTag, blank=True, help_text="Select applicable quick tap tags"
    )
    comment = models.TextField(blank=True, help_text="Optional comment from the client")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.star_rating} Stars for {self.worker.user.phone_number}"


class JobRequest(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Declined", "Declined"),
        ("Completed", "Completed"),
    ]

    # client_id linking back to the User model
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="job_requests_made",
    )

    # worker_profile_id linking to the WorkerProfile
    worker_profile = models.ForeignKey(
        "WorkerProfile", on_delete=models.CASCADE, related_name="job_requests_received"
    )

    required_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True
    )  # Crucial for FR3.5 Earnings Tracking

    def __str__(self):
        return f"Job for {self.worker_profile.user.phone_number} on {self.required_date} - {self.status}"
