"""
Compose transformations from reusable groups of options.

>>> [option.name for option in thumbnail.options]
['quality', 'format', 'resize']
>>> [option.name for option in base.options]
['quality', 'format']
"""

from imgproxykit import Transform
from imgproxykit.options import Resize

# Define reusable groups of processing options.
base = Transform(quality=85, format='webp')
square = Transform(Resize.fill(width=300, height=300))

# Combine options from both transformations.
thumbnail = base.extend(*square.options)
