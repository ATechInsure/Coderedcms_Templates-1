from .base import *  # noqa
import environ

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env(BASE_DIR.joinpath(".env"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_CACHE = False

RECAPTCHA_PUBLIC_KEY = env('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = env('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_REQUIRED_SCORE = env('RECAPTCHA_REQUIRED_SCORE')

try:
    from .local_settings import *  # noqa
except ImportError:
    pass

print(BASE_DIR.joinpath(".env"))
