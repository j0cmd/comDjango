from .settings import *

DEBUG = True

#  crie a secret key para seu ambiente de teste
SECRET_KEY = 'ixb6fh&#ts=&bt$au%pgp_62-!8dw2j==j)d^3-j$!z(@*m+-h'

DATABASES = {
    'default': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}
