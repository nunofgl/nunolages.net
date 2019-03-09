"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
import getpass

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

#HOME_DIR = HOME_DIR = '/home/' + getpass.getuser()

os.environ['PYTHON_EGG_CACHE'] = '/tmp'

#sys.path.append(HOME_DIR+'/Sites/mysite')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
