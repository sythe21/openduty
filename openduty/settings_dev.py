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

BASE_URL = "http://opsweekly2.ipvs-graph.cloud.twc.net:8000"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'devsecret'

PAGINATION_DEFAULT_PAGINATION = 3



#LDAP RELATED
AUTH_LDAP_SERVER_URI = "ldap://165.237.86.86:389"
#AUTH_LDAP_BIND_DN = ""
#AUTH_LDAP_BIND_PASSWORD = ""
AUTH_LDAP_START_TLS = False
AUTH_LDAP_BIND_AS_AUTHENTICATING_USER = True
#AUTH_LDAP_MIRROR_GROUPS = True #Mirror LDAP Groups as Django Groups, and populate them as well.
#AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Group,dc=domain,dc=com",
#    ldap.SCOPE_SUBTREE, "(&(objectClass=posixGroup)(cn=openduty*))"
#)
#AUTH_LDAP_GROUP_TYPE = PosixGroupType()

#AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=People,dc=corp,dc=twcable,dc=com",
#AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=users,dc=corp,dc=twcable,dc=com"
AUTH_LDAP_USER_DN_TEMPLATE = "%(user)s@twcable.com"
#ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

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

