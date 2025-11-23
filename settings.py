from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------------------------------

SECRET_KEY = 'django-insecure-4wxlr9ubq9jvto6151dc#tl&*o8yb302yne#1!h(-yhg24k)$-'
DEBUG = True
ALLOWED_HOSTS = []

# ---------------------------------------------------
# APPS INSTALADAS
# ---------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # App principal
    'core',
]

# ---------------------------------------------------
# MIDDLEWARE
# ---------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------------------------------------------
# URLS PRINCIPALES
# ---------------------------------------------------

ROOT_URLCONF = 'config.urls'

# ---------------------------------------------------
# TEMPLATES
# ---------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # carpeta global de templates
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

# ---------------------------------------------------
# WSGI
# ---------------------------------------------------

WSGI_APPLICATION = 'config.wsgi.application'

# ---------------------------------------------------
# BASE DE DATOS
# ---------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ---------------------------------------------------
# VALIDACIÓN DE PASSWORDS
# ---------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------------------------------------------
# IDIOMA Y ZONA HORARIA
# ---------------------------------------------------

LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'

USE_I18N = True
USE_TZ = True

# ---------------------------------------------------
# ARCHIVOS ESTÁTICOS (CSS, JS, IMÁGENES)
# ---------------------------------------------------

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",   # carpeta global para CSS, JS, imágenes
]

# ---------------------------------------------------
# ARCHIVOS DE MEDIA (subidas)
# ---------------------------------------------------

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ---------------------------------------------------
# USUARIO PERSONALIZADO
# ---------------------------------------------------

AUTH_USER_MODEL = 'core.Usuario'

# ---------------------------------------------------
# CONFIGURACIÓN DE LOGIN/LOGOUT
# ---------------------------------------------------

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'

# ---------------------------------------------------
# CONFIGURACIÓN POR DEFECTO DE MODELOS
# ---------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

