"""Production file configuration.

Simple configuration file.
"""
from core.settings.common_cloud_settings import *
import os

DEBUG = False
PRODUCTION = True
CLOUD = True
CORS_ORIGIN_WHITELIST = [
    os.environ['frontend'],
]