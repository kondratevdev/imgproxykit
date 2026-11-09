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

> Build [imgproxy](https://imgproxy.net/) URLs with typed Python options and
> reusable transformations. Define image settings once, compose them for
> different use cases, and generate named variants from a single source.

## Features

- [x] Fully typed and checked with `mypy`, `pyright`, `ty` and `pyrefly` in strict modes
- [x] Signed URLs using your `imgproxy` server's `key` and `salt`
- [x] Immutable, reusable transforms combining typed options and scalar arguments
- [x] Variants: generate multiple image URLs from a reusable set of transforms
- [x] Support for named presets configured on your `imgproxy` server
- [x] `Django`, `Django Modern REST`, `Django REST Framework`, `FastAPI`, `Litestar` integration

---------

## Installation

Requires **Python 3.12+**. A running [imgproxy](https://github.com/imgproxy/imgproxy)
server is needed to serve images from the generated URLs.

```bash
pip install imgproxykit
```

There are several included extras:

- `'imgproxykit[django]'` provides [Django](https://imgproxykit.readthedocs.io/en/latest/pages/integrations/django.html)
  and [Django-Modern-REST](https://github.com/wemake-services/django-modern-rest)
  integrations with shortcuts, template tags, and client configuration through Django settings
- `'imgproxykit[drf]'` provides [Django REST Framework integration](https://imgproxykit.readthedocs.io/en/latest/pages/integrations/drf.html)
  with serializer fields for image URLs and named variants
- `'imgproxykit[fastapi]'` provides [FastAPI integration](https://imgproxykit.readthedocs.io/en/latest/pages/integrations/fastapi.html)
  with a dependency for injecting the client into route handlers
- `'imgproxykit[litestar]'` provides [Litestar integration](https://imgproxykit.readthedocs.io/en/latest/pages/integrations/litestar.html)
  with a plugin that injects the client into route handlers

## Examples

### Generate a thumbnail URL

Build a URL for a cropped `webp` thumbnail:

```python
>>> from imgproxykit import Client, Transform
>>> from imgproxykit.options import Resize

>>> # Public URL of your imgproxy server.
>>> client = Client('https://imgproxy.example.com')

>>> thumbnail = Transform(
...     Resize.fill(width=300, height=300),  # Pass typed option objects.
...     quality=80,  # Or scalar keywords, equivalent to Quality(80).
...     format='webp',
... )

>>> source_url = 'https://originals.example.com/products/backpack.jpg'
>>> thumbnail_url = client.url(source=source_url, transform=thumbnail)

```

The generated URL has this structure, with the source URL encoded as URL-safe `base64`:

```text
https://imgproxy.example.com/unsafe/resize:fill:300:300/quality:80/format:webp/<encoded-source>
```

`thumbnail_url` points to a cropped `webp` thumbnail.

### Generate image variants

Build variants by extending a shared transform with a width for each size:

```python
>>> from imgproxykit import Client, Transform

>>> client = Client('https://imgproxy.example.com')

>>> # Share quality and output format across all variants.
>>> base = Transform(quality=85, format='webp')
>>> products = {
...     'small': base.extend(width=320),
...     'medium': base.extend(width=640),
...     'large': base.extend(width=1280),
... }

>>> source_url = 'https://originals.example.com/products/backpack.jpg'
>>> # Build one URL per variant for the same source image.
>>> product_urls = client.variants(source=source_url, variants=products)

```

`product_urls` maps each variant name to its generated URL:

```text
{
    'small': 'https://imgproxy.example.com/unsafe/quality:85/format:webp/width:320/<encoded-source>',
    'medium': 'https://imgproxy.example.com/unsafe/quality:85/format:webp/width:640/<encoded-source>',
    'large': 'https://imgproxy.example.com/unsafe/quality:85/format:webp/width:1280/<encoded-source>',
}
```

## Next steps

- Read the [documentation](https://imgproxykit.readthedocs.io/en/latest/)
  for client configuration, transformations, variants, and processing options.
- Check the [changelog](https://imgproxykit.readthedocs.io/en/latest/pages/changelog.html)
  for new features, fixes, and breaking changes.
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
