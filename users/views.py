from django.shortcuts import render

from .models import Profile


def profile(request):
    return render(request, "account/profile.html")
