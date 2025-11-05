import os

from dotenv import load_dotenv

load_dotenv()

host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
key = os.getenv('DB_SECRET_KEY')

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
