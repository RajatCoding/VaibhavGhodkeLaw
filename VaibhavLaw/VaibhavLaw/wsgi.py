"""
WSGI config for VaibhavLaw project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.conf import settings
# print(settings.configure())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VaibhavLaw.settings')

application = get_wsgi_application()
