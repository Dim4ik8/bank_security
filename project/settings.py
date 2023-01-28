import os

from environs import Env

env = Env()
env.read_env()

ENGINE = env('ENGINE')
HOST = env('HOST')
PORT = env.int('PORT')
NAME = env('NAME')
USER_ID = env('USER_ID')
PASSWORD = env('PASSWORD')


DATABASES = {
    'default': {
        'ENGINE': ENGINE,
        'HOST': HOST,
        'PORT': PORT,
        'NAME': NAME,
        'USER': USER_ID,
        'PASSWORD': PASSWORD,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

DEBUG = env.bool('DEBUG')


ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
