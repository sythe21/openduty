"""
Django settings for openduty project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery
import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType
djcelery.setup_loader()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

BROKER_URL = 'django://'

LOGIN_URL = '/login/'

PROFILE_MODULE = 'openduty.UserProfile'

#LDAP RELATED
AUTH_LDAP_SERVER_URI = "ldap://165.237.86.86:389"
AUTH_LDAP_START_TLS = False
AUTH_LDAP_BIND_AS_AUTHENTICATING_USER = True
AUTH_LDAP_USER_DN_TEMPLATE = "%(user)s@twcable.com"

AUTH_LDAP_USER_ATTR_MAP = {
"first_name": "uid",
"last_name": "sn",
"email": "mail"
}


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'kombu.transport.django',
    'openduty',
    'openduty.templatetags',
    'schedule',
    'djcelery',
    'notification',
    'django_tables2',
    'django_tables2_simplefilter',
    'bootstrap3',
    "django_twilio"
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'openduty.middleware.basicauthmiddleware.BasicAuthMiddleware',
)

ROOT_URLCONF = 'openduty.urls'

WSGI_APPLICATION = 'openduty.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FIRST_DAY_OF_WEEK = 1

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
       'rest_framework.permissions.IsAuthenticated',
    ),
    'PAGINATE_BY': 10
}

PAGINATION_DEFAULT_PAGINATION = 20 # The default amount of items to show on a page if no number is specified.

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT =  os.path.realpath(os.path.dirname(__file__))+"/static/"
STATICFILES_DIRS = (
    os.path.realpath(os.path.dirname(__file__))+'/static_schedule/',
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

AUTH_PROFILE_MODULE = 'openduty.UserProfile'

BASE_URL = "http://openduty.ipvs-graph.cloud.twc.net"

XMPP_SETTINGS = {
}

EMAIL_SETTINGS = {
}

TWILIO_SETTINGS = {
}

SLACK_SETTINGS = {
}

PROWL_SETTINGS = {
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'openduty',
        'USER': 'openduty',
        'PASSWORD': 'kungfupow1',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            "init_command": "SET storage_engine=MyISAM",
         }
    }
}

TWILIO_ACCOUNT_SID = TWILIO_SETTINGS.get("SID", "disabled")
TWILIO_AUTH_TOKEN = TWILIO_SETTINGS.get("token", "disabled")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kungfusecret'

import sys
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test_sqlite.db',
        }
    }


    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
        'django.contrib.auth.hashers.SHA1PasswordHasher',
    )
