from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, PhoneLoginForm


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log the user in after registration
            login(request, user)
            return redirect(
                "core:client_dashboard"
            )  # Redirect to the dashboard we built earlier
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = PhoneLoginForm(request, data=request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=phone_number, password=password)
            if user is not None:
                login(request, user)
                return redirect("core:client_dashboard")
    else:
        form = PhoneLoginForm()

    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("accounts:login")
