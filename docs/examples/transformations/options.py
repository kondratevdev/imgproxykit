"""
Combine option instances and scalar keyword arguments.

>>> [option.name for option in thumbnail.options]
['resize', 'quality', 'format']
>>> thumbnail.options == explicit.options
True
"""

from imgproxykit import Transform
from imgproxykit.options import Format, Quality, Resize

thumbnail = Transform(
    Resize(width=300, height=300, mode='fill'),
    quality=85,
    format='webp',
)
explicit = Transform(
    Resize(width=300, height=300, mode='fill'),
    Quality(85),
    Format('webp'),
)
