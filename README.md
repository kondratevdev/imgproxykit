<h1 align="center">imgproxykit</h1>

<p align="center">
  <em>A typed Python toolkit for building imgproxy URLs.</em>
</p>

<div align="center">

[![Tests Result](https://github.com/kondratevdev/imgproxykit/actions/workflows/test.yml/badge.svg?event=push)](https://github.com/kondratevdev/imgproxykit/actions/workflows/test.yml)
[![PyPI Version](https://img.shields.io/pypi/v/imgproxykit.svg)](https://pypi.org/project/imgproxykit/)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/imgproxykit.svg)](https://pypi.org/project/imgproxykit/)
[![Typing](https://img.shields.io/badge/typing-typed-35544A.svg)](https://github.com/kondratevdev/imgproxykit/blob/master/imgproxykit/py.typed)
[![License](https://img.shields.io/badge/license-MIT-35544A.svg)](LICENSE)

</div>

<p align="center">
  <a href="#features">Features</a> ·
  <a href="#installation">Installation</a> ·
  <a href="#example">Example</a> ·
  <a href="https://github.com/kondratevdev/imgproxykit/issues">Issues</a> ·
  <a href="CONTRIBUTING.md">Contributing</a>
</p>

<p align="center">
  Define image transformations in Python. Build reusable, signed URLs.<br>
  Let your imgproxy server fetch and process the images.
</p>

---------

## Features

- [x] Fully typed and checked with `mypy`, `pyright`, and `pyrefly`
- [x] Reusable transforms built from typed processing options
- [x] Automatic URL signing with your imgproxy key and salt
- [x] Free imgproxy processing options
- [x] Output format selection, including WebP and AVIF
- [x] Support for named presets configured on your imgproxy server

---------

## Installation

Requires **Python 3.12+** and a running imgproxy server.

```bash
pip install imgproxykit
```

## Example

Create a Retina-ready product card with smart cropping and WebP output:

```python
from imgproxykit import Client, Transform
from imgproxykit.options import (
    DPR,
    Format,
    Gravity,
    Quality,
    Resize,
    Sharpen,
    StripMetadata,
)

imgproxy = Client('https://imgproxy.your-app.com')

card = Transform(
    Resize(width=400, height=400, mode='fill'),
    Gravity(position='sm'),
    DPR(2),
    Quality(80),
    Sharpen(0.5),
    StripMetadata(True),
    Format('webp'),
)

url = imgproxy.url(
    'https://storage.your-app.com/sneakers.jpg',
    transform=card,
)
```

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
