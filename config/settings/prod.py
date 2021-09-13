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

DEBUG = False
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


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
DATABASES['default']['ATOMIC_REQUESTS'] = True


###########
# Logging #
###########

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # Logging format
    'formatters': {
        'production': {
            'format': '%(asctime)s [%(levelname)s] %(process)d %(thread)d '
                      '%(pathname)s:%(lineno)d %(message)s'
        },
    },
    # ハンドラ
    'handlers': {
        # Log file output setting
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/{}/app.log'.format(PROJECT_NAME),
            'formatter': 'production',
        },
    },
    'loggers': {
        # All logs
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        # Django logs
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
