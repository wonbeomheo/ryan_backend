from .base import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangoweb_prod',
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PW"),
        'HOST': 'localhost',
        'PORT': '5432'
    }
}