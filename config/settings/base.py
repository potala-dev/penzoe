from pathlib import Path

import dj_database_url
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    ALLOWED_HOSTS=(list, []),
    ANYMAIL_ACCOUNT_DEFAULT_HTTP_PROTOCOL=(str, "https"),
    CSRF_COOKIE_SECURE=(bool, True),
    DATABASE_CONN_MAX_AGE=(int, 600),
    DATABASE_SSL_REQUIRE=(bool, True),
    DEBUG=(bool, False),
    DEBUG_TOOLBAR=(bool, False),
    DJSTRIPE_WEBHOOK_VALIDATION=(str, "verify_signature"),
    EMAIL_BACKEND=(str, "anymail.backends.sendgrid.EmailBackend"),
    EMAIL_TESTING=(bool, False),
    ROLLBAR_ENABLED=(bool, True),
    ROLLBAR_ENVIRONMENT=(str, "production"),
    SECURE_HSTS_PRELOAD=(bool, True),
    SECURE_HSTS_SECONDS=(int, 60 * 60 * 24 * 365),
    SECURE_SSL_REDIRECT=(bool, True),
    SESSION_COOKIE_SECURE=(bool, True),
    SLACK_WEBHOOK=(str, ""),
    STRIPE_LIVE_MODE=(bool, True),
)
env_file = BASE_DIR / ".env"
if env_file.is_file():
    environ.Env.read_env(str(env_file))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")
ADMIN_PATH = env("ADMIN_PATH")

DEBUG = env("DEBUG")
DEBUG_TOOLBAR = env("DEBUG_TOOLBAR")

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

# App constants
domain = "penzoe.herokuapp.com"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # 3rd party
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.google",
    "rest_framework",
    # Local
    "penzoe.core",
    "penzoe.users",
    "penzoe.discourse",
    "penzoe.words",
    "penzoe.quiz",
]


CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        conn_max_age=env("DATABASE_CONN_MAX_AGE"),
        ssl_require=env("DATABASE_SSL_REQUIRE"),
    )
}

# Starting in Django 3.2, the default field is moving to BigAutoField,
# but I don't want to mess with a bunch of migrations in 3rd party apps.
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

AUTH_USER_MODEL = "users.User"

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# django.contrib.sites
SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media/"

# django-allauth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True


LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"


# GITHUB
GITHUB_TOKEN = env("GITHUB_TOKEN")
GITHUB_ORG = env("GITHUB_ORG")
GITHUB_BOOK_CATALOG = env("GITHUB_BOOK_CATALOG")
