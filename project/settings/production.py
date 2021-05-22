import django_heroku

from .base import *  # noqa: F403

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_USER")  # noqa: F405
EMAIL_HOST_PASSWORD = env("EMAIL_PASS")  # noqa: F405

django_heroku.settings(locals(), databases=False)
