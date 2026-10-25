from imgproxykit import Transform
from imgproxykit.integrations.django import SettingsDict

thumbnail = Transform(width=300, height=300, format='webp')

IMGPROXYKIT: SettingsDict = {
    'client': {
        'base_url': 'https://imgproxy.example.com',
        # Use your server's key and salt.
        'key': '736563726574',
        'salt': '73616c74',
    },
    'transforms': {'thumbnail': thumbnail},
    'variants': {
        'product': {
            'small': thumbnail,
            'large': Transform(width=1280, format='webp'),
        },
    },
}
