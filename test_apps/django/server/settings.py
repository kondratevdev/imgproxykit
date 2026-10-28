from pathlib import Path

from imgproxykit import Transform
from imgproxykit.integrations.django import SettingsDict

SECRET_KEY = 'imgproxykit-test-project'  # noqa: S105

ALLOWED_HOSTS = (
    'localhost',
    '127.0.0.1',
    'testserver',
)

INSTALLED_APPS = (
    'imgproxykit.integrations.django',
    'rest_framework',
)

ROOT_URLCONF = 'server.urls'

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (Path(__file__).parent / 'templates',),
        'APP_DIRS': True,
    },
)

WSGI_APPLICATION = 'server.wsgi.application'

# The test app has no authentication models or database.
REST_FRAMEWORK = {  # noqa: WPS407
    'DEFAULT_AUTHENTICATION_CLASSES': (),
    'UNAUTHENTICATED_USER': None,
}

_SMALL = Transform(width=320, format='webp')
_MEDIUM = Transform(width=640, format='webp')
_LARGE = Transform(width=1280, format='webp')

# Match the local imgproxy service configured in docker-compose.yaml.
IMGPROXYKIT: SettingsDict = {  # noqa: WPS407
    'client': {
        'base_url': 'http://localhost:10002',
        'key': '736563726574',
        'salt': '73616c74',
    },
    'transforms': {'preview': _MEDIUM},
    'variants': {
        'responsive': {
            'small': _SMALL,
            'medium': _MEDIUM,
            'large': _LARGE,
        },
    },
}
