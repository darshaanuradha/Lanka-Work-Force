from django.shortcuts import render
from .models import Category, WorkerProfile


def client_dashboard(request):
    """
    Handles the main demand-side interface (FR2.1 & FR2.2).
    Displays categories and a list of currently online workers.
    """
    # Fetch all labor categories for the visual buttons
    categories = Category.objects.all()

    # Fetch only workers who have their status set to Online
    available_workers = WorkerProfile.objects.filter(is_online=True).select_related(
        "user", "category"
    )

    context = {
        "categories": categories,
        "workers": available_workers,
    }

    return render(request, "client_dashboard.html", context)
