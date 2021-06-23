"""
WSGI config for life0 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from dj_static import  Cling
from django.core.wsgi import get_wsgi_application
#from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bootcamp.settings")

#application = get_wsgi_application()
#application = DjangoWhiteNoise(application)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "life0.settings")

application = Cling(get_wsgi_application())
