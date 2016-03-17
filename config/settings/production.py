from .base import *

import dj_database_url

#######################
# DEBUG CONFIGURATION #
#######################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#std:setting-DEBUG
DEBUG = env('DJANGO_DEBUG', False)

##########################
# SECURITY CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#secret-key
# This key should only be used for development and testing!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#secure-content-type-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = True

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#x-frame-options
X_FRAME_OPTIONS = 'DENY'

##########################
# DATABASE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
# https://github.com/kennethreitz/dj-database-url#usage
DATABASES = dj_database_url.config()

# https://docs.djangoproject.com/en/{{ docs_version }}/topics/db/transactions/#tying-transactions-to-http-requests
DATABASES['default']['ATOMIC_REQUESTS'] = True

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/databases/#persistent-connections
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#std:setting-CONN_MAX_AGE
DATABASES['default']['CONN_MAX_AGE'] = 60

#######################
# CACHE CONFIGURATION #
#######################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
    }
}

##########################
# TEMPLATE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#std:setting-TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(APPS_DIR, 'templates')],
        'OPTIONS': {
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ])
            ],
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#############################
# STATIC FILE CONFIGURATION #
#############################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#staticfiles-storage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

######################
# HOST CONFIGURATION #
######################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#allowed-hosts
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = []

#########################
# LOGGING CONFIGURATION #
#########################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#logging
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/logging/#configuring-logging
# TK
