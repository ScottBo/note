"""
WSGI config for wiki project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "note.settings")
sys.path.insert(0,os.path.dirname(__file__))
from django.core.handlers import wsgi
application=wsgi.WSGIHandler()
