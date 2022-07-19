from server.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

BASE_URL = 'http://localhost:8080'
