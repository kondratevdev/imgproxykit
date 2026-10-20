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

---------

## Installation

Requires **Python 3.12+** and a running imgproxy server.

```bash
pip install imgproxykit
```

## Example

Build a URL for a WebP thumbnail served by your imgproxy server:

```python
from imgproxykit import Client, Transform
from imgproxykit.options import Resize

client = Client('https://imgproxy.your-app.com')  # Your imgproxy server.

thumbnail = Transform(
    Resize(width=300, height=300, mode='fill'),  # Pass option objects.
    quality=80,  # Or scalar, equivalent to Quality(80).
    format='webp',
)
thumbnail_url = client.url(
    'https://example.com/photo.jpg',
    transform=thumbnail,
)
```

Use `thumbnail_url` in an image's `src`; imgproxy handles the image processing.

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
