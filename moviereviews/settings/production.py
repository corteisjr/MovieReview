from .settings import *

ALLOWED_HOSTS = ['127.0.0.1']
DEBUG = False
SECRECT_KEY = 'he2n8e2qj@7!zi$6jf=z08ncd&1v8ltqv+xvo!vn%&mab8(0ez'

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.sqlite3',
        'Name': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}