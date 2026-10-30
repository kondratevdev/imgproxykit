"""
Create new transformations by adding processing options.

>>> [option.name for option in base.options]
['quality', 'format']
>>> [option.name for option in thumbnail.options]
['quality', 'format', 'resize']
>>> [option.name for option in retina.options]
['quality', 'format', 'resize', 'dpr']
"""

from imgproxykit import Transform
from imgproxykit.options import Resize

# Share quality and output format across transformations.
base = Transform(quality=85, format='webp')

# Add a square crop without changing the base transformation.
thumbnail = base.extend(Resize(width=300, height=300, mode='fill'))

# Create a higher pixel density version of the thumbnail.
retina = thumbnail.extend(dpr=2)
