"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import django_heroku
import os
import getpass

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY is set as a Heroku config variable 

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG set to False in production, set to True in local environment 
# TEMPLATE_DEBUG = set to False in production, set to True in local environment

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'nunolages.net', 'afternoon-earth-65611.herokuapp.com']


SITE_ID = os.getenv("SITE_ID")

# ON_HEROKU is an env variable defined in Heroku, but not locally
# fetch these variables defined locally only if not running on Heroku but with manage.py
# Heroku will inject it's own variables
if 'ON_HEROKU' not in os.environ: 
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")
    DEBUG = os.getenv("DEBUG")
    TEMPLATE_DEBUG = os.getenv("TEMPLATE_DEBUG")

# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_comments',
    'tagging',
    'mptt',
    'zinnia',
    'intro',
    'intro_pt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                # Couldn't import this one in the command line. Is it valid?
                'django.contrib.messages.context_processors.messages',
                'zinnia.context_processors.version',  # Optional
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "Europe/Lisbon"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR + "/static/"),
)

STATICFILES_FINDERS = ( 
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.template.context_processors.i18n',
  'django.template.context_processors.request',
  'zinnia.context_processors.version',  # Optional
)


TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Activate Django-Heroku.
django_heroku.settings(locals())


