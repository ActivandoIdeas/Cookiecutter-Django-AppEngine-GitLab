"""Kumpel API Views.

Show the main page application.
"""
from django.http import HttpResponse


def main_page():
    """View for link app.

    Main view app
    """
    return HttpResponse("Django app with Activando Ideas Template for GitLab and GCP")
