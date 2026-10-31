imgproxykit
===========

A typed Python toolkit for building imgproxy URLs.

Define reusable image transformations, generate signed URLs, and create
named variants for thumbnails, avatars, and previews.

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

.. literalinclude:: /examples/getting_started/transformations.py
   :language: python
   :show-output:
   :lines: 1-13

.. code-annotations::

   1. Public URL of your imgproxy server. Replace it with your own address.
   2. URL of the original image. Replace it with an image URL accessible
      to your imgproxy server.
   3. Build the URL without making a network request. Imgproxy fetches and
      processes the source image when the generated URL is requested.

Use ``thumbnail_url`` in an image's ``src`` attribute or an API response.
Reuse ``thumbnail`` with other source images to apply the same transformation.

.. tip::

    URL generation makes no network requests. Your imgproxy server fetches
    and processes the image when the generated URL is requested. You need
    a running imgproxy server to serve images.

Find your way
-------------

* :doc:`pages/getting-started` walks through installation and your first
  image URLs.
* :doc:`User guide <pages/user-guide/client>` introduces the client,
  transformations, processing options, and named variants.
* :doc:`Django integration <pages/integrations/django>` configures a shared
  client and generates URLs from model file fields.
* :doc:`Django Modern REST <pages/integrations/dmr>` returns image URLs and
  variants from typed controllers.
* :doc:`DRF integration <pages/integrations/drf>` returns image URLs and
  variants from serializer fields.
* :doc:`FastAPI integration <pages/integrations/fastapi>` registers clients
  as application dependencies.
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
    pages/user-guide/variants

.. toctree::
    :caption: Integrations
    :maxdepth: 2
    :hidden:

    pages/integrations/django
    pages/integrations/dmr
    pages/integrations/drf
    pages/integrations/fastapi

.. toctree::
    :maxdepth: 2
    :hidden:

    pages/api-reference/index
    pages/changelog
