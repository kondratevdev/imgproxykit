imgproxykit
===========

A typed Python toolkit for building imgproxy URLs.
Define reusable image transformations and generate signed URLs or reference
presets configured on your imgproxy server.

.. _quick-start:

Quick start
-----------

Install imgproxykit with Python 3.12 or newer:

.. code-block:: bash

    pip install imgproxykit

Create a Retina-ready product card with smart cropping and WebP output:

.. code-block:: python

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
        Sharpen(value=0.5),
        StripMetadata(value=True),
        Format('webp'),
    )

    url = imgproxy.url(
        'https://storage.your-app.com/sneakers.jpg',
        transform=card,
    )

Reuse ``card`` for other source images. URL generation makes no network
requests: imgproxy fetches and processes the image when the URL is requested.

.. note::

    Without signing credentials, URLs use the ``unsafe`` marker.
    For a server with signature checking enabled, pass both ``key`` and
    ``salt`` to ``Client``. See :doc:`pages/usage`.

.. toctree::
    :maxdepth: 2
    :caption: Documentation

    pages/usage
    pages/changelog

.. toctree::
    :caption: API Reference
    :hidden:

    pages/api-reference/index
