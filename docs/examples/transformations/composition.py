"""
Build new transformations from shared options.

>>> [option.name for option in base.options]
['quality', 'format']
>>> [option.name for option in product_thumbnail.options]
['quality', 'format', 'width']
>>> avatar.options[-1].arguments
('fill', 96, 96, None, None)
"""

from imgproxykit import Transform
from imgproxykit.options import Resize

base = Transform(quality=85, format='webp')

product_thumbnail = Transform(*base.options, width=320)
avatar = Transform(
    *base.options,
    Resize(width=96, height=96, mode='fill'),
)
