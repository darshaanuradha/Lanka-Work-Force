from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    # The empty string '' means this is the default page for the app
    path("", views.client_dashboard, name="client_dashboard"),
]
