import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Chat',
        'USER': 'Dauren',
        'PASSWORD': 'sungat97',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}


STATIC_DIR = os.path.join(BASE_DIR,'static')
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'