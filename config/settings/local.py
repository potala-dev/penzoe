"""Django local settings for penzoe project."""

from .base import *  # noqa: F403

INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa: F405
INTERNAL_IPS = ["127.0.0.1"]

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
