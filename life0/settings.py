"""
Django settings for life0 project.

Generated by 'django-admin startproject' using Django 1.11.29.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from datetime import timedelta
import  datetime
import  dj_database_url

import  django_heroku




# Configure app for Heroku deployment


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6)am1we7!xq8u@2*h8b%4g5&vjq0@z9x2#x)2&*c=f4bf2xwd('
AUTH_USER_MODEL = 'api.User'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
    #True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://localhost:44385",
    "http://localhost:4205",
    "http://127.0.0:4205",
    "http://localhost:3001",
    "http://127.0.0.1:3001",
    "https://socialrecipehome.netlify.app",
    "https://recipes147homi.netlify.app",
    "https://depwebpack1.herokuapp.com",

]
ALLOWED_HOSTS = ["*",'127.0.0.1','https://depwebpack1.herokuapp.com']
CORS_ORIGIN_ALLOW_ALL = True

STREAM_API_KEY = '3mmmubkzuat4'
STREAM_API_SECRET = 'u6vh3ggypwpgck6jvyf65u7gecuh37fxwy2nu5czmhkb4dr93ba7mf7jkknz838d'
CORS_ALLOW_CREDENTIALS = True
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    "reciepe",
    "api",
    #'knox',
    'myprofile0',
    "registration",
    'account',
    'userprofile',
    'forum',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'salesman.core',
    'recipevideo',
    'polls',
    'ingredient',
    'music',
    'chat',
    'cart0',
    'core',
    'food1',
    'myfood',
   # 'django.contrib.comments',
    'corsheaders',
    'salesman.basket',
    'salesman.checkout',
    'salesman.orders',
    'salesman.admin',
     'shop',
    'mycometchatter',
    'feed',
    'story',
    'rest_framework',

'rest_framework.authtoken',
    'rest_auth',
     'contactus',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'life0.middleware.dev_cors_middleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'life0.urls'
#STATICFILES_STORAGE='whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'life0.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'life0',
        'USER': 'postgres',
        'PASSWORD': 'ayoub',
        'HOST': 'localhost',
        'PORT': '5432',
        'CONN_MAX_AGE': 500,
    }
}
# Password validation  shopl
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
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
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
       # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',

        'rest_framework.permissions.IsAuthenticated',
      #  'knox.auth.TokenAuthentication',
    ),
   # 'DEFAULT_PARSER_CLASSES': [
   #     'rest_framework.parsers.JSONParser',
    #],

    'DATETIME_FORMAT': "%m/%d/%Y %H:%M:%S",
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'life0.utils.my_jwt_response_handler',
    'JWT_ALLOW_REFRESH': False,
#'JWT_REFRESH_EXPIRATION_DELTA': timedelta(hours=1),
'JWT_EXPIRATION_DELTA': datetime.timedelta(days=2),
'JWT_VERIFY_EXPIRATION': False,
    # allow refreshing of tokens
    'JWT_ALLOW_REFRESH': True,

    # this is the maximum time AFTER the token was issued that
    # it can be refreshed.  exprired tokens can't be refreshed.
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
}
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
#REST_USE_JWT = True
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ayoubjobs.2019@gmail.com' #your email-id
EMAIL_HOST_PASSWORD = 'sahar+ayoub1' #your password
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'

SALESMAN_PRODUCT_TYPES = {
    'shop.Product': 'shop.serializers.ProductSerializer',
}

SALESMAN_PAYMENT_METHODS = [
    'shop.payment.PayInAdvance',
   # 'shop.payment.PayOnDelivery',
    'shop.payment.CreditCardPayment',
]

SALESMAN_BASKET_MODIFIERS = [
    'shop.modifiers.DiscountModifier',
    'shop.modifiers.SpecialTaxModifier',
    'shop.modifiers.ShippingCostModifier',
]

#LOGIN_REDIRECT_URL = '/'
#CRISPY_TEMPLATE_PACK = 'bootstrap4'
django_heroku.settings(locals(), staticfiles=False)