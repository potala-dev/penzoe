from enum import auto

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Confidence(models.TextChoices):
    Good = "G", _("Good")
    Average = "A", _("Average")
    Bad = "B", _("Bad")


class Word(models.Model):
    form = models.CharField(max_length=20)
    confidence = models.CharField(max_length=1, choices=Confidence.choices)
    learning_started = models.DateTimeField(auto_now_add=True)
    last_revised = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
