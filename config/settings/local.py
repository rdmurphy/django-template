# -*- coding: utf-8 -*-

from .base import *

import dj_database_url

#######################
# DEBUG CONFIGURATION #
#######################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#std:setting-DEBUG
DEBUG = env('DJANGO_DEBUG', True)

############################
# SECRET KEY CONFIGURATION #
############################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#secret-key
# This key should only be used for development and testing!
SECRET_KEY = env('DJANGO_SECRET_KEY', 'this_is_my_development_key')

##########################
# DATABASE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
# https://github.com/kennethreitz/dj-database-url#usage
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://localhost/{{ project_name }}')
}

# https://docs.djangoproject.com/en/{{ docs_version }}/topics/db/transactions/#tying-transactions-to-http-requests
DATABASES['default']['ATOMIC_REQUESTS'] = True

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
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

######################################
# DJANGO DEBUG TOOLBAR CONFIGURATION #
######################################

if not env('DISABLE_DEBUG_TOOLBAR', False):
    INSTALLED_APPS += (
        'debug_toolbar',
    )

###################################
# DJANGO EXTENSIONS CONFIGURATION #
###################################

INSTALLED_APPS += (
    'django_extensions',
)
