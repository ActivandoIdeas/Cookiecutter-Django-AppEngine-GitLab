"""Urls for project.

Link to admin, show dashboard and main page.
"""
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import main_page

urlpatterns = [
    path('', main_page),
]
