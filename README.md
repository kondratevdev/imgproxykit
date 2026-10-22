<h1 align="center">imgproxykit</h1>

<p align="center">
  <em>A typed Python toolkit for building imgproxy URLs.</em>
</p>

<div align="center">

[![Tests Result](https://img.shields.io/github/actions/workflow/status/kondratevdev/imgproxykit/test.yml?branch=master&label=tests&labelColor=black&color=blue)](https://github.com/kondratevdev/imgproxykit/actions/workflows/test.yml)
[![PyPI Version](https://img.shields.io/pypi/v/imgproxykit.svg?labelColor=black&color=blue)](https://pypi.org/project/imgproxykit/)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/imgproxykit?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=BLUE&left_text=downloads)](https://pepy.tech/projects/imgproxykit)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/imgproxykit.svg?labelColor=black&color=blue)](https://pypi.org/project/imgproxykit/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?labelColor=black)](LICENSE)

</div>

## Features

- [x] Fully typed and checked with `mypy`, `pyright`, `ty` and `pyrefly` in strict modes
- [x] Expressive transforms: combine option objects with concise scalar arguments
- [x] Immutable, reusable transforms for consistent image settings across your app
- [x] Support for named presets configured on your imgproxy server

---------

## Installation

Requires **Python 3.12+** and a running imgproxy server.

```bash
pip install imgproxykit
```

## Example

Define a WebP thumbnail once and reuse it across a product catalog:

```python
from imgproxykit import Client, Transform
from imgproxykit.options import Gravity, Resize

# Public URL of your imgproxy server.
client = Client('https://imgproxy.example.com')

thumbnail = Transform(
    Resize(width=300, height=300, mode='fill'),  # Pass typed option objects.
    Gravity(position='sm'),  # Let imgproxy choose the crop's focus.
    quality=80,  # Or scalar keywords, equivalent to Quality(80).
    format='webp',
)
source_urls = [
    'https://originals.example.com/products/backpack.jpg',
    'https://originals.example.com/products/sneakers.jpg',
]
# Reuse one immutable transformation across your catalog.
thumbnail_urls = [
    client.url(source=source_url, transform=thumbnail)
    for source_url in source_urls
]
```

Use these URLs in your images' `src` attributes. Building a URL makes no
network requests: when a browser requests it, imgproxy fetches the original
image from `originals.example.com` and processes it.

Sign URLs and reuse presets configured on your imgproxy server:

```python
from imgproxykit import Client, Transform
from imgproxykit.options import Preset

client = Client(
    'https://imgproxy.example.com',
    # Replace with your imgproxy server's hex-encoded key and salt.
    key='736563726574',
    salt='73616c74',
)

thumbnail = Transform(
    Preset('product-card'),  # Reuse a preset from your imgproxy server.
    format='webp',  # Combine server presets with explicit processing options.
)
source_url = 'https://originals.example.com/products/backpack.jpg'
# The client signs the URL using your server's key and salt.
thumbnail_url = client.url(source=source_url, transform=thumbnail)
```

See the [full documentation](https://imgproxykit.readthedocs.io/en/latest/)
for client configuration, transformations, and processing options.
Find published releases on [PyPI](https://pypi.org/project/imgproxykit/).

## Contributing

See the [contributing guide](CONTRIBUTING.md) for development setup and checks.
Bug reports and feature requests are welcome on the
[issue tracker](https://github.com/kondratevdev/imgproxykit/issues).

## License

[MIT](LICENSE)

## Credits

Generated with
[`wemake-python-package`](https://github.com/wemake-services/wemake-python-package)
([template version](https://github.com/wemake-services/wemake-python-package/tree/47d9dddd29da8d6d3d1a403f8a143b323a812083)).
