from settings import *

DEBUG = True
TEMPLATE_DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
import sys
if 'test' not in sys.argv:
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

BASE_URL = "http://openduty.ipvs-graph.cloud.twc.net"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'devsecret'

PAGINATION_DEFAULT_PAGINATION = 3



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

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'openduty.middleware.basicauthmiddleware.BasicAuthMiddleware',
)

