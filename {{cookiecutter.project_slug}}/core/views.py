"""Main views."""
from django.shortcuts import render


def handler404(request, *args, **argv):
    """Error 404 configuration."""
    return render(request, '{{cookiecutter.project_slug}}/404.html')


def handler500(request, *args, **argv):
    """Error 500 configuration."""
    return render(request, '{{cookiecutter.project_slug}}/404.html')
