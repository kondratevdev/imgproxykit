imgproxykit
===========

A typed Python toolkit for building imgproxy URLs.

Describe image transformations in Python and generate signed URLs for your
imgproxy server. Reuse the same settings across product cards, avatars,
and image previews.

Build your first URL
--------------------

Install imgproxykit with Python 3.12 or newer:

.. code-block:: bash

    pip install imgproxykit

Create a client pointing to your imgproxy server and pass a source image URI:

.. literalinclude:: /examples/getting_started/first_url.py
   :language: python
   :start-at: from imgproxykit

Continue with :doc:`pages/getting-started` to resize images, choose an output
format, and sign URLs.

.. tip::

    URL generation makes no network requests. Your imgproxy server fetches
    and processes the image when the generated URL is requested. You need
    a running imgproxy server to serve images.

What you can do
---------------

* **Reuse transformations.** Define a ``Transform`` once and use it for
  different source images.
* **Configure processing in Python.** Combine typed option classes and scalar
  keyword arguments for dimensions, formats, quality, and other settings.
* **Sign URLs.** Use your server's key and salt, or generate unsigned URLs
  when your server accepts them.
* **Reference server presets.** Combine named imgproxy presets with explicit
  processing options.

Find your way
-------------

* :doc:`pages/getting-started` walks through installation and your first
  image URLs.
* :doc:`pages/user-guide/index` explains client configuration, transformations,
  and choosing processing options.
* :doc:`pages/api-reference/index` lists classes, arguments, types,
  and extension points.
* :doc:`pages/changelog` tracks releases and compatibility changes.

.. toctree::
    :maxdepth: 2
    :hidden:

    pages/getting-started
    pages/user-guide/index
    pages/api-reference/index
    pages/changelog
