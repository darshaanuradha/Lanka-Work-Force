from django.shortcuts import render
from .models import Category, WorkerProfile, JobRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import WorkerProfileForm


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


@login_required
def worker_dashboard(request):
    """
    Handles the supply-side interface (FR3.1, FR3.2).
    Displays the worker's status toggle and incoming job requests.
    """
    # Security check: Ensure clients don't end up here
    if request.user.active_role != "Worker":
        return redirect("core:client_dashboard")

    # Try to get the worker profile.
    # (Note: In a real app, if this doesn't exist, you'd redirect them to a "Complete Your Profile" form first)
    try:
        profile = request.user.worker_profile
    except WorkerProfile.DoesNotExist:
        # For testing, we'll pass None if they haven't set up their category/rate yet
        profile = None

    pending_jobs = []
    if profile:
        # Fetch jobs where status is 'Pending'
        pending_jobs = JobRequest.objects.filter(
            worker_profile=profile, status="Pending"
        ).order_by("-created_at")

    context = {
        "profile": profile,
        "pending_jobs": pending_jobs,
    }

    return render(request, "worker_dashboard.html", context)


@login_required
def worker_onboarding(request):
    """
    Handles the profile creation for newly registered workers.
    """
    # Security check 1: Only workers belong here
    if request.user.active_role != "Worker":
        return redirect("core:client_dashboard")

    # Security check 2: If they already have a profile, send them to the dashboard
    if hasattr(request.user, "worker_profile"):
        return redirect("core:worker_dashboard")

    if request.method == "POST":
        form = WorkerProfileForm(request.POST)
        if form.is_valid():
            # commit=False means "wait, don't save to the database just yet!"
            profile = form.save(commit=False)

            # Attach the currently logged-in user to this new profile
            profile.user = request.user

            # Now save it to the database
            profile.save()
            return redirect("core:worker_dashboard")
    else:
        form = WorkerProfileForm()

    return render(request, "worker_onboarding.html", {"form": form})
