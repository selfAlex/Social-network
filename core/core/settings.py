import os

from pathlib import Path
from envs import env

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'y+$w$u45@%c2de$^4v1gb^&8h9v!_ikgdsg59cbqt6nh($*2bl'

DEBUG = True

ALLOWED_HOSTS = ['192.168.1.22']

INSTALLED_APPS = [

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'app.apps.MyAppConfig'

]

AUTH_USER_MODEL = 'app.User'

LOGIN_URL = 'index_page'

MIDDLEWARE = [

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware'

]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [],
        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.request",
            ],
        },
    },
]

DATABASES = {

    'default': {
        
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'social-network',
        'USER': 'postgres',
        'PASSWORD': 'super',
        'HOST': '127.0.0.1',
        'PORT': '5432',

    }

}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Almaty'

STATIC_URL = '/static/'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = env('EMAIL')
EMAIL_HOST_PASSWORD = env('PASSWORD')
EMAIL_PORT = 587
