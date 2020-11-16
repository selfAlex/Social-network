from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'y+$w$u45@%c2de$^4v1gb^&8h9v!_ikgdsg59cbqt6nh($*2bl'

DEBUG = True

INSTALLED_APPS = [

]

MIDDLEWARE = [

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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC+6'
