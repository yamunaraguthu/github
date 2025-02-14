"""
Django settings for weather project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-y@j0v&!96#dgcth$efjqbmbh&kx-cd4=ti*ac16n9bp6rp5n-4"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# from decouple import config

# GOOGLE_API_KEY = config('AIzaSyBPIvqCUFEGHd9FuxO6cqgW9W-vG3AbRiQ')
# SEARCH_ENGINE_ID = config('22ec9abca78c5406a')

# WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "767c1905e7ab50e9f6751515fd1e7d46")
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyBPIvqCUFEGHd9FuxO6cqgW9W-vG3AbRiQ")
# SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID", "22ec9abca78c5406a")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'weather_app',
    
]

# add the openweathermap API key to setting.py
# OPENWEATHERMAP_API_KEY='d07a397960b23b5c5d23c8b3599e46e4'


# WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "767c1905e7ab50e9f6751515fd1e7d46")
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyARlrB7bonzGWJp32US2Y1QVLTwu2F4IUU")
# SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID", "22ec9abca78c5406a")



MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]



ROOT_URLCONF = "weather.urls"


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],  # Add your global templates directory here
        'APP_DIRS': True,  # Enables Django to look for templates in app directories
        'OPTIONS': {
            'context_processors': [
            "django.template.context_processors.debug",
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "weather.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
# import django.core.exceptions
STATIC_URL= '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static"),
]

STATIC_ROOT=os.path.join(BASE_DIR,'assets')
# django.core.exceptions.ImproperlyConfigured
# STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
# BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles'),
         
# (statcfiles.W004) The directory 'C:\Users\yamun\OneDrive\Desktop\new django\weather\static' in the STATICFILES_DIRS setting does not exist.

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

