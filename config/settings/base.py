"""
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from os import environ, path

from django.core.exceptions import ImproperlyConfigured

######################
# PATH CONFIGURATION #
######################

# This file
BASE_FILE = path.abspath(__file__)

# Absolute filesystem path to the project directory
ROOT_DIR = path.abspath(path.join(path.dirname(BASE_FILE), '..', '..'))

# Absolute filesystem path to the Django project's app folder
APPS_DIR = path.join(ROOT_DIR, '{{ project_name }}')

###########
# HELPERS #
###########


def env(setting, default=None):
    """ Get the environment setting or return exception """
    try:
        variable = environ[setting]
        if variable == 'True':
            return True
        elif variable == 'False':
            return False
        else:
            return variable
    except KeyError:
        if default is not None:
            return default
        else:
            error_msg = ('The {} env variable was not found '
                         'and no default was set!').format(setting)
            raise ImproperlyConfigured(error_msg)

#####################
# APP CONFIGURATION #
#####################

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (

)

LOCAL_APPS = (

)

# https://docs.djangoproject.com/en/1.8/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

############################
# MIDDLEWARE CONFIGURATION #
############################

# https://docs.djangoproject.com/en/1.8/topics/http/middleware/
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

#####################
# URL CONFIGURATION #
#####################

# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-ROOT_URLCONF
ROOT_URLCONF = 'config.urls'

# https://docs.djangoproject.com/en/1.8/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

#############################
# STATIC FILE CONFIGURATION #
#############################
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# https://docs.djangoproject.com/en/1.8/ref/settings/#static-url
STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/1.8/ref/settings/#static-root
STATIC_ROOT = path.join(APPS_DIR, 'assets')

# https://docs.djangoproject.com/en/1.8/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    path.join(APPS_DIR, 'static'),
)

#########################
# GENERAL CONFIGURATION #
#########################
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# https://docs.djangoproject.com/en/1.8/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# https://docs.djangoproject.com/en/1.8/ref/settings/#time-zone
TIME_ZONE = 'UTC'

# https://docs.djangoproject.com/en/1.8/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-USE_L10N
USE_L10N = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-USE_TZ
USE_TZ = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#site-id
SITE_ID = 1
