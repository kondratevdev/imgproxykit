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

Create a client pointing to your imgproxy server and define a thumbnail
transformation:

.. note::

    The examples use ``imgproxy.example.com`` for your imgproxy server and
    ``originals.example.com`` for the original images. Replace these example
    addresses with your own.

.. literalinclude:: /examples/getting_started/transformations.py
   :language: python
   :start-at: from imgproxykit

``thumbnail_url`` is ready to use in an image's ``src`` attribute or an API
response. Reuse ``thumbnail`` with other source images to apply the same
300×300 crop and WebP format across your application.

.. tip::

    URL generation makes no network requests. Your imgproxy server fetches
    and processes the image when the generated URL is requested. You need
    a running imgproxy server to serve images.

Find your way
-------------

* :doc:`pages/getting-started` walks through installation and your first
  image URLs.
* :doc:`User guide <pages/user-guide/client>` covers client configuration,
  transformations, variants, and processing options.
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
    pages/user-guide/variants
    pages/user-guide/options

.. toctree::
    :maxdepth: 2
    :hidden:

    pages/api-reference/index
    pages/changelog
