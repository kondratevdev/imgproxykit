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
- [x] Immutable, reusable transforms combining typed options and scalar arguments
- [x] Variants: generate multiple image URLs from a reusable set of transforms
- [x] Support for named presets configured on your imgproxy server
- [x] Native `Django` integration with settings, shortcuts, and template tags
- [x] Native `FastAPI` integration with dependency injection

---------

## Installation

Requires **Python 3.12+** and a running [imgproxy](https://github.com/imgproxy/imgproxy) server.

```bash
pip install imgproxykit
```

## Examples

### Single URL

Build a URL for a cropped WebP thumbnail:

```python
>>> from imgproxykit import Client, Transform
>>> from imgproxykit.options import Resize

>>> # Public URL of your imgproxy server.
>>> client = Client('https://imgproxy.example.com')

>>> thumbnail = Transform(
...     Resize(width=300, height=300, mode='fill'),  # Pass typed option objects.
...     quality=80,  # Or scalar keywords, equivalent to Quality(80).
...     format='webp',
... )

>>> source_url = 'https://originals.example.com/products/backpack.jpg'
>>> thumbnail_url = client.url(source=source_url, transform=thumbnail)

```

`thumbnail_url` points to a 300×300 WebP thumbnail with smart cropping.
Imgproxy fetches and processes the original image when this URL is requested.

### Variants

Build variants by combining shared settings with different sizes:

```python
>>> from imgproxykit import Client, Transform

>>> client = Client('https://imgproxy.example.com')

>>> # Share quality and output format across all variants.
>>> base = Transform(quality=85, format='webp')
>>> products = {
...     'small': Transform(*base.options, width=320),
...     'medium': Transform(*base.options, width=640),
...     'large': Transform(*base.options, width=1280),
... }

>>> source_url = 'https://originals.example.com/products/backpack.jpg'
>>> # Build one URL per variant for the same source image.
>>> product_urls = client.variants(source=source_url, variants=products)
>>> small_url = product_urls['small']  # Access a URL by its variant name.

```

`product_urls` contains a URL for each size, all using the shared quality
and WebP format. Reuse `products` with other source images to keep the same
variants across your catalog.

## Next steps

- Read the [documentation](https://imgproxykit.readthedocs.io/en/latest/)
  for client configuration, transformations, variants, and processing options.
- Find published releases on [PyPI](https://pypi.org/project/imgproxykit/).

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
