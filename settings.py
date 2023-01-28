import os

from environs import Env

env = Env()
env.read_env()

ENGINE = env('ENGINE')
HOST = env('HOST')
PORT = env('PORT')
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

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
