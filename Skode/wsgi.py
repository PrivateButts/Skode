"""
WSGI config for Skode project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only
from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
from django.core.wsgi import get_wsgi_application

# Import local environmental varbs
env_path = Path('.') / 'local.env'
load_dotenv(dotenv_path=env_path)
load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Skode.settings")


application = Sentry(get_wsgi_application())
