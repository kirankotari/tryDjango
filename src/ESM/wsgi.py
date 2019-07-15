"""
<<<<<<< HEAD:src/ESM/wsgi.py
WSGI config for esm project.
=======
WSGI config for ESM project.
>>>>>>> a627f93e94f74b034daf67ca921942783e8685bd:src/ESM/wsgi.py

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'esm.settings')

application = get_wsgi_application()
