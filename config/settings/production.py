from .base import *

#######################
# DEBUG CONFIGURATION #
#######################

# https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-DEBUG
DEBUG = env('DJANGO_DEBUG', False)

############################
# SECRET KEY CONFIGURATION #
############################

# https://docs.djangoproject.com/en/1.9/ref/settings/#secret-key
# This key should only be used for development and testing!
SECRET_KEY = env('SECRET_KEY')

##########################
# DATABASE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# https://docs.djangoproject.com/en/1.9/topics/db/transactions/#tying-transactions-to-http-requests
DATABASES['default']['ATOMIC_REQUESTS'] = True

#######################
# CACHE CONFIGURATION #
#######################

# https://docs.djangoproject.com/en/1.9/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

##########################
# TEMPLATE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(APPS_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ])
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

######################
# HOST CONFIGURATION #
######################

# https://docs.djangoproject.com/en/1.9/ref/settings/#allowed-hosts
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['*']
