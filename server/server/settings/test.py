from server.settings.base import *

DEBUG = False

SECRET_KEY = "TEST_RUNNING"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
