from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.splash_screen, name="splash_screen"),
    # The empty string '' means this is the default page for the app
    path("client/", views.client_dashboard, name="client_dashboard"),
    path("worker/", views.worker_dashboard, name="worker_dashboard"),
    # NEW: The onboarding route
    path("worker/onboarding/", views.worker_onboarding, name="worker_onboarding"),
]
