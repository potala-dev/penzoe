"""Django local settings for penzoe project."""

from .base import *  # noqa: F403

if DEBUG and DEBUG_TOOLBAR:  # noqa: F405
    INSTALLED_APPS.append("debug_toolbar")  # noqa: F405
    MIDDLEWARE.insert(  # noqa: F405
        0, "debug_toolbar.middleware.DebugToolbarMiddleware"
    )
    INTERNAL_IPS = ["127.0.0.1"]

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
