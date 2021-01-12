from pathlib import Path
from envs import env

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'y+$w$u45@%c2de$^4v1gb^&8h9v!_ikgdsg59cbqt6nh($*2bl'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1:8000', '192.168.1.22:8000']

INSTALLED_APPS = [

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'rest_framework',
    'rest_framework.authtoken',

    'app.apps.MyAppConfig'
]

AUTH_USER_MODEL = 'app.User'

LOGIN_URL = 'index_page'

MIDDLEWARE = [

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
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

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '654079109227-aqfphtn6mfqif8cgjgtu6rumksolc2oj.apps.googleusercontent.com',
            'secret': 'xwo2v6kt9ZX5d9aH_QePBQw5',
            'key': ''
        }
    }
}

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

LOGIN_REDIRECT_URL = '/'

REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
