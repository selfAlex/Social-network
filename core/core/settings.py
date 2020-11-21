from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'y+$w$u45@%c2de$^4v1gb^&8h9v!_ikgdsg59cbqt6nh($*2bl'

DEBUG = True

ALLOWED_HOSTS = ['192.168.1.22']

INSTALLED_APPS = [

    'django.contrib.auth',
    'django.contrib.contenttypes',

    'app.apps.MyAppConfig'

]

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Almaty'
