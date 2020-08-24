"""Django local settings for penzoe project."""

from .base import *

if DEBUG and DEBUG_TOOLBAR:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = ["127.0.0.1"]

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
