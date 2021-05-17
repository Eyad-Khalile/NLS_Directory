"""
Django settings for nls_world_map project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from django.conf import settings
import os
from decouple import config
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "0121#gy^92ovph$(*=ze7-@sr$h(9@#*q32de5d4$6$3a5w2m5"
# SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['https://nls-directory.com/',
                 'www.nls-directory.com/', 'nls-directory.com/', '127.0.0.1']
# ALLOWED_HOSTS = [config('MAIN_HOST'), '127.0.0.1']


# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'map_app',
    'members',
    'crispy_forms',
    'django_filters',
    'phone_field',
    'cart.apps.CartConfig',
    'mptt',
    'fontawesome-free',
    'import_export',
    'widget_tweaks',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'members.authentication.EmailAuthbackend',
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nls_world_map.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates/',)
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nls_world_map.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'NLS_Directory_DB',
#         'USER': 'admin_eyad',
#         'PASSWORD': 'EyadPacha79@',
#         'HOST': 'piriro.han-solo.net',
#         'PORT': '3306',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# SESSION AGE
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30  # One month


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]


LANGUAGES = [
    ('ar', _('عربي')),
    ('fr', _('Françes')),

]


CRISPY_TEMPLATE_PACK = 'bootstrap4'

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# =============== STATIC CONFIG ===============
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


# ON PROD
STATIC_ROOT = (os.path.join(BASE_DIR, 'static/'))

# ON DEV
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

# =============== MEDIA CONFIG ===============
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')


LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# AUTH_USER_MODEL = "members.CustomUser"

# ===== SMTP EMAIL CONFIGURATIONS ===========
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST          = 'mail.nls-directory.com'
# EMAIL_HOST          = 'smtp.gmail.com'
# EMAIL_HOST        = 'smtp02.hostnet.nl'
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True
EMAIL_HOST_USER     = 'info@nls-directory.com'
EMAIL_HOST_PASSWORD = 'Ismainfo11=2021%'


# CART SESSION
CART_SESSION_ID = 'cart'


# HTTPS SETTINGS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS SETTINGS
SECURE_HSTS_SECONDS = 31536000 # 1 YEAR
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
