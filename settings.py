import os

from dotenv import load_dotenv

load_dotenv()

host = os.getenv('HOST')
port = os.getenv('PORT')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
key = os.getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': host,
        'PORT': port,
        'NAME': 'checkpoint',
        'USER': user,
        'PASSWORD': password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = key

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
