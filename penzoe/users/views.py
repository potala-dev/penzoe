from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ProfileUpdateForm
from .models import Profile


def profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been updated!")
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, "account/profile.html", {"form": form})
