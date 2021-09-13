from .base import *
import os
import environ

#################
# Read env file #
#################

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))


#####################
# Security settings #
#####################

DEBUG = True
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ['*']


############
# Database #
############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
    }
}


###########
# Logging #
###########

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # Logging format
    'formatters': {
        'develop': {
            'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d '
                      '%(message)s'
        },
    },
    'handlers': {
        # Console output setting
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'develop',
        },
    },
    'loggers': {
        # All logs
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Django logs
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        # DB logs
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
