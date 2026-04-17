from django import forms
from .models import WorkerProfile


class WorkerProfileForm(forms.ModelForm):
    class Meta:
        model = WorkerProfile
        # We only ask for these three things.
        # The 'user' is handled automatically in the background,
        # and 'average_rating' / 'is_online' have default values.
        fields = ["category", "location", "daily_rate"]
