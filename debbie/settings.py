import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "=;;uzYCn}{Mh=wr|@n-VIC/?|Ckj>Ef3V<WN|hxx_;rJ41*3WUU5Ll~<sC`/t27"
DEBUG = True
ALLOWED_HOSTS = []

if DEBUG:
    INTERNAL_IPS = type(str("c"), (), {"__contains__": lambda *_: True})()
else:
    INTERNAL_IPS = ["127.0.0.1"]

INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "debug_toolbar",
    "organizations",
    "leaflet",
    "djgeojson",
    "polymorphic",
    "apps.core",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "debbie.urls"

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
            ],
        },
    },
]

ASGI_APPLICATION = "debbie.asgi.application"

DATABASES = {
    "default": {
        # "ENGINE": os.environ.get(
        #     "DATABASE_ENGINE", "django.contrib.gis.db.backends.spatialite"
        # ),
        # "NAME": os.environ.get("POSTGRES_DB", BASE_DIR / "db.sqlite3"),
        # "USER": os.environ.get("POSTGRES_USER", "user"),
        # "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "password"),
        # "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        # "PORT": os.environ.get("POSTGRES_PORT", 5432),
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "debbie",
        "USER": "debbie",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": 5432,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "core.AppUser"
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/accounts/login"
LOGOUT_REDIRECT_URL = LOGIN_URL

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = os.environ.get("STATIC_URL", "/static/")
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

FIXTURE_DIRS = [BASE_DIR / "fixtures"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]

GDAL_LIBRARY_PATH = "/opt/homebrew/Cellar/gdal/3.8.5/lib/libgdal.dylib"
GEOS_LIBRARY_PATH = "/opt/homebrew/Cellar/geos/3.12.1/lib/libgeos_c.dylib"
