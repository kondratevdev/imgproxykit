from imgproxykit import Transform
from imgproxykit.integrations.django import SettingsDict

thumbnail = Transform(width=300, height=300, format='webp')

IMGPROXYKIT: SettingsDict = {
    'client': {  # (1)!
        'base_url': 'https://imgproxy.example.com',
        'key': '736563726574',  # (2)!
        'salt': '73616c74',
    },
    'transforms': {'thumbnail': thumbnail},  # (3)!
    'variants': {  # (4)!
        'product': {
            'small': thumbnail,
            'large': Transform(width=1280, format='webp'),
        },
    },
}
