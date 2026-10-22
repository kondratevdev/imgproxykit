imgproxykit
===========

A typed Python toolkit for building imgproxy URLs.

Describe image transformations in Python and generate signed URLs for your
imgproxy server. Reuse the same settings across product cards, avatars,
and image previews.

Build your first URL
--------------------

Install imgproxykit with Python 3.12 or newer:

.. md-tab-set::

  .. md-tab-item:: :iconify:`material-icon-theme:uv` uv

    .. code-block:: bash

      uv add imgproxykit

  .. md-tab-item:: :iconify:`devicon:poetry` poetry

    .. code-block:: bash

      poetry add imgproxykit

  .. md-tab-item:: :iconify:`devicon:pypi` pip

    .. code-block:: bash

      pip install imgproxykit

Create a client pointing to your imgproxy server and pass a source image URI:

.. note::

    The examples use ``imgproxy.example.com`` for your imgproxy server and
    ``originals.example.com`` for the original images. Replace these example
    addresses with your own.

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

* **Reuse transformations.** Define a :class:`~imgproxykit.Transform` once and
  use it for
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
* The user guide covers :doc:`client configuration <pages/user-guide/client>`,
  :doc:`transformations <pages/user-guide/transformations>`, and
  :doc:`processing options <pages/user-guide/options>`.
* :doc:`pages/api-reference/index` lists classes, arguments, types,
  and extension points.
* :doc:`pages/changelog` tracks releases and compatibility changes.

.. toctree::
    :maxdepth: 2
    :hidden:

    pages/getting-started

.. toctree::
    :caption: User guide
    :maxdepth: 2
    :hidden:

    pages/user-guide/client
    pages/user-guide/transformations
    pages/user-guide/options

.. toctree::
    :maxdepth: 2
    :hidden:

    pages/api-reference/index
    pages/changelog
