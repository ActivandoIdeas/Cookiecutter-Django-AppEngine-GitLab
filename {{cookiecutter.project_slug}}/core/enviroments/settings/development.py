from core.enviroments.connect import generate_key
from core.settings.base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = generate_key()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
PRODUCTION = False
CLOUD = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

ALLOWED_HOSTS = ["localhost:8000", "127.0.0.1:8000", "127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
