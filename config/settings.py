
import os
import environ
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-fallback-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()  # Reads the .env file

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = env('EMAIL_USE_TLS', cast=bool)
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'core',
    'transactions',
    'invoices',
    'users',
    'django_filters',
    'reportlab',
    'products',
    'reports',
    'report_files',
    'stock_adjustments',
    'config',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'your_db_name'),
        'USER': os.environ.get('POSTGRES_USER', 'your_db_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'your_db_password'),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise settings
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS settings
CORS_ALLOWED_ORIGINS = os.environ.get('DJANGO_CORS_ALLOWED_ORIGINS', '').split(',')

# Rest Framework Configuration
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'utils.errorHandler.custom_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security settings
ALLOWED_HOSTS = ['inventra-v2.onrender.com','127.0.0.1']


# import os
# import environ
# from pathlib import Path
# from django.db.backends.signals import connection_created
# from dotenv import load_dotenv

# # Load .env file
# load_dotenv()

# # Initialize environment variables
# env = environ.Env(
#     DJANGO_DEBUG=(bool, False)
# )
# environ.Env.read_env()  # Reads the .env file

# # Base directory
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Security settings
# SECRET_KEY = env('DJANGO_SECRET_KEY', default='your-fallback-secret-key')
# DEBUG = env.bool('DJANGO_DEBUG', default=True)
# ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])

# # Email configuration
# EMAIL_HOST = env('EMAIL_HOST')
# EMAIL_PORT = env.int('EMAIL_PORT')
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS')
# DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

# # Application definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'corsheaders',
#     'core',
#     'transactions',
#     'invoices',
#     'users',
#     'django_filters',
#     'reportlab',
#     'products',
#     'reports',
#     'report_files',
#     'stock_adjustments',
#     'config',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'config.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'config.wsgi.application'
# ASGI_APPLICATION = 'config.asgi.application'

# # Database configuration
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': env('MYSQL_DB'),
#         'USER': env('MYSQL_USER'),
#         'PASSWORD': env('MYSQL_PASSWORD'),
#         'HOST': env('MYSQL_HOST'),
#         'PORT': env('MYSQL_PORT'),
#         'OPTIONS': {
#             'charset': 'utf8',
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES', innodb_strict_mode=1",
#         },
#     }
# }

# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]

# # Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_L10N = True
# USE_TZ = True

# # Static files
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']

# # Default primary key field type
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # CORS settings
# CORS_ALLOWED_ORIGINS = env.list('DJANGO_CORS_ALLOWED_ORIGINS', default=['http://localhost:3000'])

# # Rest Framework Configuration
# REST_FRAMEWORK = {
#     'EXCEPTION_HANDLER': 'utils.errorHandler.custom_exception_handler',
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.TokenAuthentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
# }

# def activate_mysql_strict_mode(sender, connection, **kwargs):
#     if connection.vendor == 'mysql':
#         cursor = connection.cursor()
#         cursor.execute("SET SESSION sql_mode = 'STRICT_TRANS_TABLES'")

# connection_created.connect(activate_mysql_strict_mode)
