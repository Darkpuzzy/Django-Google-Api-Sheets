"""
WSGI config for serviceapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import threading
from api.db_method import main
from django.core.wsgi import get_wsgi_application
from time import sleep

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'serviceapi.settings')

"""
Starting thread for auto-updated db with Google Sheets
"""
while True:
    sleep(15)
    thr = threading.Thread(target=main(), daemon=True).start()

    application = get_wsgi_application()
