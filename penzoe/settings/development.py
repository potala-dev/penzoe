"""Django local settings for penzoe project."""

from .base import *

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
