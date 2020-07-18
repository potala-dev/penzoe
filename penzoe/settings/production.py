import django_heroku

from .base import *

DEBUG = False
DEBUG_TOOLBAR = False

ALLOWED_HOSTS = []

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS")

django_heroku.settings(locals())
