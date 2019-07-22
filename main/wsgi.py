"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys
path = '/home/LiPoWeRaD/lipowerad.pythonanywhere.com'
if path not in sys.path:
    sys.path.append(path)
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
os.environ['DB_PWD'] = 'tujh6966'

application = get_wsgi_application()