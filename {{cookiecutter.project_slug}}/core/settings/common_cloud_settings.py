"""Common cloud configuration.

For deploy on GCP.
"""
import os

from core.base_settings import *
from core.enviroments.connect import get_bucked
from core.enviroments.connect import get_connection
from core.enviroments.connect import get_domain
from core.enviroments.connect import get_key
from core.enviroments.connect import get_project_id

# pylint: disable=W0614, W0401

# FIle system on Cloud Storage

PROJECT_ROOT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir
)

GS_AUTO_CREATE_ACL = 'bucketOwnerFullControl'

# Cloud File Storage configurations
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

GS_PROJECT_ID = get_project_id()
GS_BUCKET_NAME = get_bucked()

MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_BUCKET_NAME)
MEDIA_ROOT = 'media/'

UPLOAD_ROOT = 'media/uploads/'

DOWNLOAD_URL = PROJECT_ROOT + "media/downloads"
DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")

# CORS Configurations

INSTALLED_APPS += [
    'corsheaders',
]

MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_CREDENTIALS = True

# DEFAULT Dynamic CONFIGURATIONs

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_key()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

ALLOWED_HOSTS = get_domain()

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = get_connection()