from .base import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('postgresqlName'),
        'USER': config('postgresqlUser'),
        'PASSWORD': config('postgresqlPassword'),
        'HOST': config('postgresqlHost'),
        'PORT': config('postgresqlPort')
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'