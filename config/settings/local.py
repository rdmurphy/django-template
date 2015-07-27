from .base import *

#######################
# DEBUG CONFIGURATION #
#######################

# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-DEBUG
DEBUG = env('DEBUG', True)

############################
# SECRET KEY CONFIGURATION #
############################

# https://docs.djangoproject.com/en/1.8/ref/settings/#secret-key
# This key should only be used for development and testing!
SECRET_KEY = env('SECRET_KEY', 'this_is_my_development_key')

##########################
# DATABASE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(ROOT_DIR, '{{ project_name }}.db'),
    }
}

##########################
# TEMPLATE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(APPS_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

######################################
# DJANGO DEBUG TOOLBAR CONFIGURATION #
######################################

INSTALLED_APPS += (
    'debug_toolbar',
)
