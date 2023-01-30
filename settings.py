import os

import dj_database_url
from environs import Env

env = Env()
env.read_env()

DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    ),
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('SECRET_KEY')

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
