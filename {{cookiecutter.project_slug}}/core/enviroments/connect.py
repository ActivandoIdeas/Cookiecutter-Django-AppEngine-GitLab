"""Connect settings with enviroments.

Why do you do need to connect
"""
import datetime
import os
import random
import string

import yaml
from django.conf import settings


def generate_key():
    """Generate key."""
    chars = (
        ''.join([string.ascii_letters, string.digits, string.punctuation])
            .replace("'", '')
            .replace('"', '')
            .replace('\\', '')
    )
    return ''.join([random.SystemRandom().choice(chars) for i in range(50)])


def get_password_testing():
    """Get generic password for testing data."""
    if settings.CLOUD:
        return [os.environ.get('passwordtest')]
    with open('env.yaml') as file_name:
        data = yaml.safe_load(file_name)
    return (data['test_variables']['password'],)


def get_domain():
    """Get allowed host."""
    return [os.environ.get('domain')]


def get_key():
    """Get application key."""
    return os.environ.get('key')


def get_credentials():
    """Get credentials."""
    return os.environ.get('credentials')


def get_bucked():
    """Get application bucked access."""
    return os.environ.get('gcpbucked')


def get_project_id():
    """Get application project access."""
    return os.environ.get('project')


def get_dev_connection():
    """Connect local development."""
    with open('env.yaml') as file_name:
        data = yaml.safe_load(file_name)
    return {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': data['env_variables']['database'],
            'USER': data['env_variables']['user'],
            'PASSWORD': data['env_variables']['password'],
            'HOST': data['env_variables']['host'],
            'PORT': '5432',
        }
    }


def get_connection():
    """Connect for production enviroment."""
    return {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('database'),
            'USER': os.environ.get('user'),
            'PASSWORD': os.environ.get('password'),
            'HOST': os.environ.get('host'),
            'PORT': '5432',
        }
    }
